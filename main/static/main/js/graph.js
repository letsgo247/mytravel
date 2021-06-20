let data_json2 = {}


function jsonSearch(searchKey, searchValue) {      // searchValue 를 name으로 갖는 object 리턴하는 함수
    return data_json2.filter(function (obj) {
        return Object.keys(obj).some(function () {
            return obj[searchKey] == searchValue;
        })
    });
}


fetch("/static/main/js/data.json")
    .then(response => response.json())
    .then(json => { data_json2 = json })
    .then(() => {
        
       //<visitedNumber>
        let visitedNumber = document.getElementById('visitedNumber')
        visitedNumber = Number(visitedNumber.value)
        // console.log(visitedNumber)
        const numberData = [visitedNumber, 177 - visitedNumber]
        // console.log(numberData)

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
                        backgroundColor: ['#03A9F4', 'lightgray'],
                        borderColor: 'white',
                        data: numberData
                    }]
                },

                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: '여행한 국가 비율 (국가 수 기준)',
                            font: {
                                size: 20
                            }
                        },
                        legend: {
                            display: true,                            
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








        //<visitedArea>
        let visitedArea = document.getElementById('visitedArea')
        visitedArea = Number(visitedArea.value)
        // console.log(visitedArea)
        const areaData = [visitedArea, 149390550.0 - visitedArea]
        // console.log(areaData)



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
                        backgroundColor: ['#4CAF50', 'lightgray'],
                        borderColor: 'white',
                        data: areaData
                    }]
                },

                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: '여행한 국가 비율 (면적 기준)',
                            font: {
                                size: 20
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
        const continentsCountArray = document.getElementById('continentsCountArray')
        // console.log(continentsCount.value)
        continentsCountData = continentsCountArray.value.slice(1, -1).split(',')  // string을 받아와서 불필요한 괄호 제거하고 array로 변환
        // console.log(continentsCountData)
        continentsCountData = continentsCountData.map(data => Number(data))
        // console.log(continentsCountData)




        var continentsChart = new Chart(
            document.getElementById('continentsChart'),
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
                        // backgroundColor: ['#FFEB3B', '#03A9F4', '#E040FB', '#FF5252', '#4CAF50', '#FF9800', '#3F51B5'],
                        borderColor: 'white',
                        data: continentsCountData
                    }]
                },

                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: '여행지의 대륙별 비율',
                            font: {
                                size: 20
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












        //<rankChart>
        const sortedRatioDict = document.getElementById('sortedRatioDict')
        // console.log(sortedRatioDict.value)
        sortedRatioDictData = sortedRatioDict.value.slice(2, -2).split('), (')  // string을 받아와서 불필요한 괄호 제거하고 array로 변환
        // console.log(sortedRatioDictData)

        rankLabels = sortedRatioDictData.map(data => {
            alpha3 = data.slice(1, 4)
            let obj = jsonSearch('alpha3', alpha3)[0]
            let labelKr = obj.nameKr
            return labelKr
        })
        // console.log(rankLabels)


        rankData = sortedRatioDictData.map(data => Number(data.slice(7, 13)))
        // console.log(rankData)
        var rankChart = new Chart(
            document.getElementById('rankChart'),
            {
                type: 'bar',

                data: {
                    labels: rankLabels,

                    datasets: [{
                        backgroundColor: ['#ffbe22', '#60aaf3', '#948dec', '#e53949', '#91bf39', '#fe7c02', '#4836f3'],
                        borderColor: 'white',
                        data: rankData
                    }]
                },

                options: {
                    indexAxis: 'y',
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: '%',
                                align: 'center'
                            }
                        }
                    },
                    plugins: {
                        datalabels: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: '여행 많이 간 나라 순위',
                            font: {
                                size: 20
                            }
                        },
                        legend: {
                            display: false,
                        },

                        labels: {
                            // render: 'value',
                            render: function (args) {
                                return args.value + '%';
                            },
                        }

                    }
                }
            }
        );
    })


