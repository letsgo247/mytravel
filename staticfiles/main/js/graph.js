//<number>

let number = document.getElementById('number')
number = Number(number.value)
console.log(number)
const numberData = [number, 177 - number]
console.log(numberData)

var numberChart = new Chart(
    document.getElementById('numberChart'),
    {
        type: 'pie',

        data: {
            labels: [
                '가본 나라',
                '아직 못 가본 나라'
            ],

            datasets: [{
                // label: '대륙별 비율',
                backgroundColor: ['pink', 'gray'],
                borderColor: 'white',
                data: numberData
            }]
        },

        options: {
            plugins: {
                title: {
                    display: true,
                    text: '여행한 국가 비율(국가 수 기준)',
                    font: {
                        size: 15
                    }
                },
                legend: {
                    display: true
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function (item) {
                            // console.log(item);
                            let label = item.label;
                            let value = item.parsed;
                            return label + ': ' + value + ' 개국';
                        }
                    }
                },
                labels: {
                    render: 'percent',
                    precision: 1
                }
            }
        }
    }
);





//<area>
let area = document.getElementById('area')
area = Number(area.value)
console.log(area)
const areaData = [area, 149390550.0 - area]
console.log(areaData)



var areaChart = new Chart(
    document.getElementById('areaChart'),
    {
        type: 'pie',

        data: {
            labels: [
                '가본 나라',
                '아직 못 가본 나라'
            ],

            datasets: [{
                // label: '대륙별 비율',
                backgroundColor: ['lightgreen', 'gray'],
                borderColor: 'white',
                data: areaData
            }]
        },

        options: {
            plugins: {
                title: {
                    display: true,
                    text: '여행한 국가 비율(면적 기준)',
                    font: {
                        size: 15
                    }
                },
                legend: {
                    display: true
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function (item) {
                            // console.log(item);
                            let label = item.label;
                            let value = new Intl.NumberFormat().format(item.parsed);    // 숫자 형식 콤마 추가
                            return label + ': ' + value + ' km²';
                        }
                    }
                },
                labels: {
                    render: 'percent',
                    precision: 1
                }
            }
        }
    }
);










//<continent>
const continentsRatio = document.getElementById('continentsRatio')
// console.log(continentsRatio.value)
continentsRatioData = continentsRatio.value.slice(1, -1).split(',')  // string을 받아와서 불필요한 괄호 제거하고 array로 변환
console.log(continentsRatioData)
continentsRatioData = continentsRatioData.map(data => Number(data))
console.log(continentsRatioData)




var ContinentsChart = new Chart(
    document.getElementById('ContinentsChart'),
    {
        type: 'pie',

        data: {
            labels: [
                '아시아',
                '유럽',
                '오세아니아',
                '북아메리카',
                '남아메리카',
                '아프리카',
                '남극'
            ],

            datasets: [{
                backgroundColor: ['#ffbe22', '#60aaf3', '#948dec', '#e53949', '#91bf39', '#fe7c02', '#4836f3'],
                borderColor: 'white',
                data: continentsRatioData
            }]
        },

        options: {
            plugins: {
                title: {
                    display: true,
                    text: '대륙별 비율',
                    font: {
                        size: 15
                    }
                },
                legend: {
                    display: true,
                    // font: {
                    //     size: 150
                    // }
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function (item) {
                            // console.log(item);
                            let label = item.label;
                            let value = item.parsed;
                            return label + ': ' + value + '%';
                        }
                    }
                },
                labels: {
                    render: 'percent',
                    precision: 1
                }

            }
        }
    }
);