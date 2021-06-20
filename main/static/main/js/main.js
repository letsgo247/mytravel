//<지도 파트>

const svg = d3.select('svg');

const projection = d3.geoMercator()
                        .center([0, 40])
                        .scale(200)
                        .rotate([-150,0]);
// const projection = d3.geoNaturalEarth1();
// const projection = d3.geoEqualEarth();
const pathGenerator = d3.geoPath().projection(projection);

const g = svg.append('g');

svg.call(d3.zoom().on('zoom', (event) => {
    g.attr('transform', event.transform)
}))



function nameToCode (name) {    //빈칸이나 . 있으면 클래스로 못 찾아서, purify.
    return name.replaceAll(" ","").replaceAll('.','')
}



function drawMap () {
    d3.json('/static/main/js/countries-110m.json') // or 50m
    .then(data => {
        const countries = topojson.feature(data, data.objects.countries);
        // console.log(countries.features)

        g.selectAll('path').data(countries.features)
            .enter().append('path')
            .attr('class', 'country')
            .attr('d', d=>pathGenerator(d))
            .attr('id', d=>nameToCode(d.properties.name))

    })
    .then(() => markMap())
    .then(() => showTooltip())
}


function showTooltip() {
    tooltipSelection = d3.select('body')
            .append('div')
            .attr('class', 'hover-info')
            .style('visibility', 'hidden');

        tooltipEventListeners = g.selectAll('.country')
            .on('mouseenter', ({target}) => {   // 'destructuring assignment: https://stackoverflow.com/a/33705619/8551901 (콜백 변수에 {key} 를 써주면, 들어올 변수 object의 object.target을 호출함! 여기서는 첫번째 변수인 event의 target을 불러오는 거였음!)
                tooltipSelection.style('visibility', 'visible');
            })

            .on('mousemove', ({pageX, pageY, target}) => {
                // console.log(target.__data__.properties.name);
                // console.log(filterIt(target.__data__.properties.name))
                let obj = filterIt(target.__data__.properties.name)[0]
                // console.log(obj);
                tooltipSelection
                    .style('top', `${pageY + 20}px`)
                    .style('left', `${pageX - 10}px`)
                    .style('z-index', 100)
                    .html(`<img src="${obj.url}" alt=${obj.name}> ${obj.nameKr} (${obj.name})`)  //__data__는... 대충 target을 만든 data를 출력해줌?;;
            })

            .on('mouseleave', ({target}) => {
                tooltipSelection.style('visibility', 'hidden');
            })
}


function markMap() {
    if (document.querySelector('#countriesArray')) {
        // console.log('있네 있어')
        selectedArrayString = document.querySelector('#countriesArray').value;
        // console.log(selectedArrayString);
        selectedArray = selectedArrayString.slice(1, -1).split(', ')  // string을 받아와서 불필요한 괄호 제거하고 array로 변환
        // console.log(selectedArray)
        selectedArray.forEach(d => {
            // console.log(d)
            code = nameToCode(d.slice(1, -1))
            // console.log(code)
            selected = document.querySelector(`#${code}`)
            // console.log(selected)
            selected.classList.add('selected');
        })
    }
    
    else {
        // console.log('index인가벼...')
    }
}




// <이모지 로딩 위한 빌드업>
let data_json = {}

fetch("/static/main/js/data.json")    // 이름 안맞는 애들 나중에 수작업으로 고치려고 emoji.json 따로 받아둠
  .then(response => response.json())
  .then(json => {data_json = json})
  .then(() => drawMap())


// window.addEventListener('DOMContentLoaded', markMap())


function filterIt(searchValue) {      // searchValue 를 name으로 갖는 object 리턴하는 함수
    return data_json.filter(function(obj) {
        return Object.keys(obj).some(function() {
        return obj['name'] == searchValue;
        })
    });
}



// <array handling 파트>

const gLayer = document.querySelector('g')
const ol = document.querySelector('ol')
// console.log(gLayer);
// console.log(ol);
const countriesArray = [];
// const liArray = [];

function gLayer_listener () {
    gLayer.addEventListener('click', event=>{
    let data = event.target.__data__;

    let name = data.properties.name;
    code = nameToCode(name)   //빈칸이나 . 있으면 클래스로 못 찾아서, purify.
    
    if (countriesArray.includes(name)) { 
        //기존에 있으면
        removeCountry(name,code)

    } else {
        //기존에 없으면
        addCountry(event,name,code)
    }})
}



function addCountry (event,name,code) {
    //일단 색깔 칠하고
    event.target.classList.add('selected');
    // event.target.id = code;  // 미리 모든 나라에 달아둠
    // event.target.setAttribute('style', 'fill:orange')

    //어레이에 추가
    countriesArray.push(name);

    //리스트에 추가
    const li = document.createElement('li');
    li.classList = code;
    url = filterIt(name)[0].url
    nameKr = filterIt(name)[0].nameKr
    li.innerHTML = `<img src="${url}" alt=${name}> ${nameKr}`
    ol.appendChild(li);

    // liArray.push(li.innerHTML);

    //추가된 리스트에 휴지통 method 추가
    hover_listener(li,name,code);
}




function removeCountry (name,code) {
    //일단 색깔 지우고
    target = document.querySelector(`#${code}`);
    target.classList.remove('selected')

    //어레이에서 삭제
    let idx = countriesArray.indexOf(name);
    if (idx > -1) countriesArray.splice(idx, 1);
    
    //리스트에서 삭제
    const li = document.querySelector(`li.${code}`)
    ol.removeChild(li);

    let innerHTML = li.innerHTML
    
    if (innerHTML.includes('/span')) {
        // console.log(true);
        innerHTML = innerHTML.slice(0,-17);
    }   // 휴지통으로 삭제 시 list의 span 땜에 에러나는거 방지용!

    // let idx2 = liArray.indexOf(innerHTML);
    // if (idx2 > -1) liArray.splice(idx2,1);
}





// <수동 post 파트>
function submit_listener () {   // 선택된 array ajax 처리로 post 보내주는 함수!!!
    $('.submit').on('mouseover', () => {
        $('.input')[0].value = countriesArray
        // console.log($('.input')[0].value)

        // $('.input2')[0].value = liArray
        // console.log($('.input2')[0].value)


    })
}






// <휴지통 파트>
function hover_listener (li,name,code) {
    li.addEventListener('mouseenter', () => {
        span = ' <span>🗑️</span>'
        li.innerHTML += span

        const can = document.querySelector('ol span')
        can.addEventListener('click', (event) => {
            removeCountry(name,code)
        })
    })

    li.addEventListener('mouseleave', () => {
        li.innerHTML = li.innerHTML.replace(span,'')
    })
}



Kakao.init('84d8fd6fde6bfa9abdb90d8b5557c9d6');
// console.log(Kakao)


function kakaoInit() {
    // console.log('실행?')
    console.log(window.location.href)   // 현재 열려있는 url

    Kakao.Link.sendDefault({
        // container: ".kakao-link", // 공유하기 기능을 부여할 DOM container
        objectType: "feed", // 피드타입
        content: {
          title: "여최몇?",
          description:
            "그 동안 여행했던 나라를 모두 선택해주세요! 재미있는 통계 결과를 알려드립니다.",
          imageUrl:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/World_Map_Blank.svg/2753px-World_Map_Blank.svg.png",
          link: {
            webUrl: `${window.location.href}`, // 카카오 PC에서 확인할 때 연결될 웹 url
            mobileWebUrl: `${window.location.href}`, // 카카오 앱에서 확인할 때 연결될 웹 url
          },
        },
      });
}




function init() {
    if (document.querySelector('#countriesArray')) {}   // result로 가서 countriesArray가 있으면 pass, 아니면 아래 listener 실행하기
    else {
        gLayer_listener();
        submit_listener();
    }
}

init();