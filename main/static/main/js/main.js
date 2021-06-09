//<지도 파트>

const svg = d3.select('svg');

const projection = d3.geoMercator();
const pathGenerator = d3.geoPath().projection(projection);

const g = svg.append('g');

svg.call(d3.zoom().on('zoom', (event) => {
    g.attr('transform', event.transform)
}))


d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json')
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
                tooltipSelection
                    .style('top', `${pageY + 20}px`)
                    .style('left', `${pageX - 10}px`)
                    .style('z-index', 100)
                    .text(target.__data__.properties.name)  //__data__는... 대충 target을 만든 data를 출력해줌?;;
            })

            .on('mouseleave', ({target}) => {
                tooltipSelection.style('visibility', 'hidden');
            })
        })







// <이모지 로딩 위한 빌드업>
let emojiJson = {}

fetch("./static/main/js/emoji.json")    // 이름 안맞는 애들 나중에 수작업으로 고치려고 emoji.json 따로 받아둠
  .then(response => response.json())
  .then(json => {emojiJson = json})


function filterIt(searchValue) {      // searchValue 를 갖는 object 리턴하는 함수
return emojiJson.filter(function(obj) {
    return Object.keys(obj).some(function(key) {
    return obj[key].includes(searchValue);
    })
});
}






// <array handling 파트>

const gLayer = document.querySelector('g')
const ol = document.querySelector('ol')
// console.log(gLayer);
// console.log(ol);
const array = [];

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

    //어레이에 추가
    array.push(name);   

    //리스트에 추가
    const li = document.createElement('li');
    li.classList = code;
    flag = filterIt(name)[0].emoji
    li.innerHTML = `${flag} ${name}`
    ol.appendChild(li);

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
}





// <Ajax 파트>
function submit_listener () {   // 선택된 array ajax 처리로 post 보내주는 함수!!!
    $('.submit').on('click', () => {
        console.log('submit!')

        $.ajax(
            {
                type:"POST",
                url:"./",
                data: {array: array},
                dataType: "text",
            }
        ).done(() => {alert("성공!")})
        .fail(() => {alert("실패ㅠ")})
    })
};






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