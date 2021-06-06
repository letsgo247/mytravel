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
//            .append('title')
//            .text(d => d.properties.name)

        tooltipSelection = d3.select('body')
            .append('div')
            .attr('class', 'hover-info')
            .style('visibility', 'hidden');

        tooltipEventListeners = g.selectAll('.country')
            .on('mouseenter', ({target}) => {   // 'destructuring assignment: https://stackoverflow.com/a/33705619/8551901 (콜백 변수에 {key} 를 써주면, 들어올 변수 object의 object.target을 호출함! 여기서는 첫번째 변수인 event의 target을 불러오는 거였음!)
                tooltipSelection.style('visibility', 'visible');
                d3.select(target)
                    .style('fill', 'gold');
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
                d3.select(target)
                    .style('fill', d3.select(target).classed('selected') ? 'orange' : 'ivory')
            })


        clickListeneres = g.selectAll('.country')
            .on('click', ({target}) => {
                d3.select(target)
                    .classed('selected', d3.select(target).classed('selected') ? false : true)
                    .style('fill', 'orange');
                    console.log(target)

            })

        g.selectAll('.selected')


        })











//기존 파트

const button = document.querySelector('main')
const ol = document.querySelector('ol')
// console.log(ol);
const array = [];

function button_listener () {
    button.addEventListener('click', event=>{
    // console.log(event.target.innerText);
    let code = event.target.classList[0];
    let name = event.target.innerText

    let node = document.querySelector(`.${code}`);
    node.classList.toggle('selected');
    
    if (array.includes(code)) {
        //있으면
        //어레이에서 삭제
        //리스트에서 삭제
        let idx = array.indexOf(code);
        if (idx > -1) array.splice(idx, 1);

        const li = document.querySelector(`li.${code}`)
        console.log(li)
        ol.removeChild(li);


    } else {
        //없으면
        //어레이에 추가
        //리스트에 추가
        array.push(code);

        const li = document.createElement('li');
        console.log(li)
        li.classList = code;
        li.innerText = name;
        ol.appendChild(li);
        
    }
    console.log(code,name);
    console.log(array)

    })
}


function init() {
    button_listener()
}

//init();   //일단 꺼둠.