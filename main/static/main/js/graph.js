// data 파트
const continentsRatio = document.getElementById('continentsRatio')
// console.log(continentsRatio.value)
continentsRatioData = continentsRatio.value.slice(1, -1).split(',')  // string을 받아와서 불필요한 괄호 제거하고 array로 변환
// console.log(continentsRatioData)






// 그래프 파트

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
                // label: '대륙별 비율',
                backgroundColor: ['#ffbe22', '#60aaf3', '#948dec', '#e53949', '#91bf39', '#fe7c02', '#4836f3'],
                borderColor: 'white',
                data: continentsRatioData
            }]
        },

        options: {
            plugins: {
                title: {
                    display: true,
                    text: '대륙별 비율'
                },
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function(item) {
                            // console.log(item);
                            let label = item.label;
                            let value = item.parsed;
                            return label+': '+value+'%';
                        }
                    }
                }
            }
        }
    }
);