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

init();