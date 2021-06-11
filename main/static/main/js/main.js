//<지도 파트>

const svg = d3.select('svg');

const projection = d3.geoMercator()
                        .center([-30, 30])
                        .scale(300)
                        .rotate([-150,0]);
// const projection = d3.geoNaturalEarth1();
// const projection = d3.geoEqualEarth();
const pathGenerator = d3.geoPath().projection(projection);

const g = svg.append('g');

svg.call(d3.zoom().on('zoom', (event) => {
    g.attr('transform', event.transform)
}))


d3.json('./static/main/js/countries-110m.json')
    .then(data => {
        const countries = topojson.feature(data, data.objects.countries);

        g.selectAll('path').data(countries.features)
            .enter().append('path')
            .attr('class', 'country')
            .attr('d', d=>pathGenerator(d))

        tooltipSelection = d3.select('body')
            .append('div')
            .attr('class', 'hover-info')
            .style('visibility', 'hidden');

        tooltipEventListeners = g.selectAll('.country')
            .on('mouseenter', ({target}) => {   // 'destructuring assignment: https://stackoverflow.com/a/33705619/8551901 (콜백 변수에 {key} 를 써주면, 들어올 변수 object의 object.target을 호출함! 여기서는 첫번째 변수인 event의 target을 불러오는 거였음!)
                tooltipSelection.style('visibility', 'visible');
            })

            .on('mousemove', ({pageX, pageY, target}) => {
                let obj = filterIt(target.__data__.properties.name)[0]
                tooltipSelection
                    .style('top', `${pageY + 20}px`)
                    .style('left', `${pageX - 10}px`)
                    .style('z-index', 100)
                    .html(`<img src="${obj.url}" alt=${obj.name}> ${obj.nameKr} (${obj.name})`)  //__data__는... 대충 target을 만든 data를 출력해줌?;;
            })

            .on('mouseleave', ({target}) => {
                tooltipSelection.style('visibility', 'hidden');
            })
        })







// <이모지 로딩 위한 빌드업>
let dataJson = {}

fetch("./static/main/js/data.json")    // 이름 안맞는 애들 나중에 수작업으로 고치려고 emoji.json 따로 받아둠
  .then(response => response.json())
  .then(json => {dataJson = json})


function filterIt(searchValue) {      // searchValue 를 갖는 object 리턴하는 함수
    return dataJson.filter(function(obj) {
        return Object.keys(obj).some(function(key) {
        return obj[key] == searchValue;
        })
    });
}






// <array handling 파트>

const gLayer = document.querySelector('g')
const ol = document.querySelector('ol')
// console.log(gLayer);
// console.log(ol);
const array = [];
const array2 = [];

function gLayer_listener () {
    gLayer.addEventListener('click', event=>{
    let data = event.target.__data__;

    let name = data.properties.name;
    let code = name.replaceAll(" ","").replaceAll('.','')   //빈칸이나 . 있으면 클래스로 못 찾아서, purify.
    
    if (array.includes(name)) { 
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
    event.target.id = code;
    // event.target.setAttribute('style', 'fill:orange')

    //어레이에 추가
    array.push(name);

    //리스트에 추가
    const li = document.createElement('li');
    li.classList = code;
    url = filterIt(name)[0].url
    nameKr = filterIt(name)[0].nameKr
    li.innerHTML = `<img src="${url}" alt=${name}> ${nameKr}`
    ol.appendChild(li);

    array2.push(li.innerHTML);

    //추가된 리스트에 휴지통 method 추가
    hover_listener(li,name,code);
}




function removeCountry (name,code) {
    //일단 색깔 지우고
    target = document.querySelector(`#${code}`);
    target.classList.remove('selected')

    //어레이에서 삭제
    let idx = array.indexOf(name);
    if (idx > -1) array.splice(idx, 1);
    
    //리스트에서 삭제
    const li = document.querySelector(`li.${code}`)
    ol.removeChild(li);

    let innerHTML = li.innerHTML
    
    if (innerHTML.includes('/span')) {
        console.log(true);
        innerHTML = innerHTML.slice(0,-17);
    }   // 휴지통으로 삭제 시 list의 span 땜에 에러나는거 방지용!

    let idx2 = array2.indexOf(innerHTML);
    if (idx2 > -1) array2.splice(idx2,1);
}





// <수동 post 파트>
function submit_listener () {   // 선택된 array ajax 처리로 post 보내주는 함수!!!
    $('.submit').on('mouseover', () => {
        $('.input')[0].value = array
        console.log($('.input')[0].value)

        $('.input2')[0].value = array2
        console.log($('.input2')[0].value)


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




function init() {
    gLayer_listener()
    submit_listener()
}

init();