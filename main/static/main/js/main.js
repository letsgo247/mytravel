const button = document.querySelector('main')
const ol = document.querySelector('ol')
// console.log(ol);
const array = [];


const svg = d3.select('svg');

const projection = d3.geoMercator();
const pathGenerator = d3.geoPath().projection(projection);

const g = svg.append('g');

svg.call(d3.zoom().on('zoom', (event) => {
    g.attr('transform', event.transform)
}))

d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json')
    .then(data => {
        const countries = topojson.feature(data, data.objects.countries);

        g.selectAll('path').data(countries.features)
            .enter().append('path')
            .attr('class', 'country')
            .attr('d', d=>pathGenerator(d))
            .append('title')
            .text(d => d.properties.name)
        })


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

init();