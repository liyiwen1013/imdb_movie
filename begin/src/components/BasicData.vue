<template>
<div>
    <div>
        <div class="name">每年上映电影可视化分析</div>
        <v-chart :options="options1" style="display: inline-block; margin: 50px 150px; width: 970px; height: 500px;" />
        <v-chart :options="options2" style="display: inline-block; margin: 50px 150px; width: 970px; height: 500px;" />
        <v-chart :options="options3" style="display: inline-block; margin: 50px 150px; width: 970px; height: 500px;" />
        <div class="name" style="margin: 100px">电影类型可视化分析</div>
        <v-chart :options="options5" style="display: inline-block; margin: 20px 150px; width: 970px; height: 500px;" />
        <v-chart :options="options4" style="display: inline-block; margin: 80px 150px; width: 970px; height: 500px;" />
        <div class="name" style="margin-top: 40px">电影情节关键字词云图</div>
        <div>
            <img src="../assets/img/词云图.png" alt="词云图" style="margin: 0 250px; width: 800px; height: 500px;" />
        </div>
    </div>
</div>
</template>

<script>
import Axios from 'axios';
// import 'echarts-wordcloud';
export default {
    data() {
        return {
            options1: {
                title: {
                    text: '票房、成本、利润'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    }
                },
                legend: {
                    data: ['数量', '票房', '成本', '利润']
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    name: "年份",
                    boundaryGap: false,
                    data: []
                },
                yAxis: [{
                    name: "金额"
                }],
                series: [{
                        name: '数量',
                        type: 'line',
                        stack: 'Total',
                        areaStyle: {},
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
                    },
                    {
                        name: '票房',
                        type: 'line',
                        stack: 'Total',
                        areaStyle: {},
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
                    },
                    {
                        name: '成本',
                        type: 'line',
                        stack: 'Total',
                        areaStyle: {},
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
                    },
                    {
                        name: '利润',
                        type: 'line',
                        stack: 'Total',
                        areaStyle: {},
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
                    }
                ]
            },
            options2: {
                title: {
                    text: '电影颜色'
                },
                legend: {},
                tooltip: {
                    trigger: 'axis',
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    },
                },
                dataset: {
                    source: []
                },
                xAxis: {
                    type: 'category'
                },
                yAxis: {
                    gridIndex: 0,
                    name: "数量"
                },
                series: [{
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: {
                        focus: 'series'
                    }
                }, {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: {
                        focus: 'series'
                    }
                }, {
                    type: 'line',
                    smooth: true,
                    seriesLayoutBy: 'row',
                    emphasis: {
                        focus: 'series'
                    }
                }]
            },
            options3: {
                title: {
                    text: 'imdb平均评分'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    formatter: function (arg) {
                        console.log(arg)
                        return arg[0].name + ' imdb评分' + arg[0].data
                    },
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    },
                },
                xAxis: {
                    name: '年份',
                    position: 'bottom',
                    offset: 15,
                    nameLocation: 'end',
                    nameTextStyle: {
                        color: "#000",
                        padding: [5, 0, 0, -5],
                    },
                    nameGap: 15,
                    nameRotate: 0,
                    data: []
                },
                yAxis: {
                    name: "评分"
                },
                series: {
                    data: [],
                    type: 'line',
                    smooth: true
                }
            },
            options4: {
                baseOption: {
                    timeline: {
                        axisType: 'category',
                        autoPlay: true,
                        playInterval: 1000,
                        data: [
                            '1990', '1991', '1992', '1993', '1994',
                            '1995', '1996', '1997', '1998', '1999',
                            '2000', '2001', '2002', '2003', '2004', '2005',
                            '2006', '2007', '2008', '2009', '2010',
                            '2011', '2012', '2013', '2014', '2015', '2016'
                        ]
                    },
                    color: ['#003366'],
                    tooltip: {},
                    calculable: true,
                    grid: {
                        top: 60,
                        left: 24,
                        right: 40,
                        bottom: 80,
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {
                                type: 'shadow',
                                label: {
                                    show: true,
                                    formatter: function (params) {
                                        return params.value.replace('\n', '');
                                    }
                                }
                            }
                        }
                    },
                    xAxis: [{
                        'type': 'category',
                        'axisLabel': {
                            'interval': 1
                        },
                        'data': [
                            'Documentary', 'Thriller', 'Science Fiction', 'Music',
                            'History', 'Horror', 'Drama', 'Mystery',
                            'Comedy', 'Adventure', 'Romance', 'Fantasy',
                            'Action', 'Crime', 'War', 'Western', 'Family'
                        ],
                        splitLine: {
                            show: false
                        },
                        name: '类型'
                    }],
                    yAxis: [{
                        type: 'value',
                        name: '电影数量'
                    }],
                    series: [{
                        name: '电影数量',
                        type: 'bar'
                    }]
                },
                options: [{
                        title: {
                            text: '1990年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 5, 3, 2, 0, 4, 5, 0, 1, 4, 3, 2, 5, 0, 2, 0, 1]
                        }]
                    },
                    {
                        title: {
                            text: '1991年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 5, 7, 2, 0, 2, 6, 1, 2, 7, 1, 0, 7, 2, 1, 0, 3]
                        }]
                    },
                    {
                        title: {
                            text: '1992年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 3, 5, 3, 3, 3, 9, 1, 6, 3, 2, 2, 5, 1, 0, 2, 0]
                        }]
                    },
                    {
                        title: {
                            text: '1993年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 8, 4, 0, 5, 5, 10, 2, 8, 10, 4, 2, 9, 3, 3, 1, 2]
                        }]
                    },
                    {
                        title: {
                            text: '1994年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 7, 8, 0, 1, 8, 8, 2, 6, 6, 2, 5, 8, 2, 1, 1, 2]
                        }]
                    },
                    {
                        title: {
                            text: '1995年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 8, 6, 2, 1, 3, 10, 1, 5, 7, 5, 3, 7, 3, 0, 2, 1]
                        }]
                    },
                    {
                        title: {
                            text: '1996年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 7, 8, 3, 3, 7, 10, 1, 9, 7, 3, 6, 12, 6, 0, 0, 2]
                        }]
                    },
                    {
                        title: {
                            text: '1997年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 9, 6, 1, 0, 5, 10, 1, 5, 10, 6, 4, 10, 3, 1, 2, 4]
                        }]
                    },
                    {
                        title: {
                            text: '1998年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 3, 5, 1, 0, 7, 9, 2, 8, 7, 6, 4, 7, 4, 2, 0, 0]
                        }]
                    },
                    {
                        title: {
                            text: '1999年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 7, 4, 2, 2, 6, 11, 0, 13, 9, 3, 5, 8, 3, 1, 0, 4]
                        }]
                    },
                    {
                        title: {
                            text: '2000年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 11, 4, 0, 0, 9, 12, 0, 10, 6, 3, 3, 7, 4, 1, 1, 2]
                        }]
                    },
                    {
                        title: {
                            text: '2001年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 8, 5, 0, 2, 6, 11, 1, 12, 10, 3, 2, 11, 3, 3, 0, 2]
                        }]
                    },
                    {
                        title: {
                            text: '2002年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 9, 5, 0, 0, 7, 10, 2, 11, 8, 5, 3, 8, 4, 0, 2, 4]
                        }]
                    },
                    {
                        title: {
                            text: '2003年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 11, 5, 1, 1, 2, 13, 0, 11, 10, 4, 4, 11, 6, 0, 0, 5]
                        }]
                    },
                    {
                        title: {
                            text: '2004年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 10, 5, 2, 3, 6, 13, 1, 12, 5, 7, 6, 9, 11, 1, 1, 4]
                        }]
                    },
                    {
                        title: {
                            text: '2005年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 12, 7, 2, 3, 3, 26, 3, 14, 13, 11, 10, 17, 8, 2, 1, 8]
                        }]
                    },
                    {
                        title: {
                            text: '2006年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 18, 4, 0, 1, 3, 20, 5, 26, 9, 9, 9, 21, 13, 2, 1, 6]
                        }]
                    },
                    {
                        title: {
                            text: '2007年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 34, 5, 1, 3, 6, 37, 4, 23, 11, 17, 8, 25, 20, 3, 1, 6]
                        }]
                    },
                    {
                        title: {
                            text: '2008年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 36, 9, 4, 4, 6, 57, 6, 37, 14, 21, 10, 22, 17, 2, 0, 8]
                        }]
                    },
                    {
                        title: {
                            text: '2009年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 41, 19, 2, 3, 10, 53, 18, 38, 23, 21, 10, 37, 24, 0, 0, 9]
                        }]
                    },
                    {
                        title: {
                            text: '2010年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [0, 25, 13, 4, 4, 9, 76, 12, 61, 21, 31, 13, 25, 20, 4, 0, 14]
                        }]
                    },
                    {
                        title: {
                            text: '2011年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 39, 20, 4, 5, 15, 91, 20, 84, 13, 42, 11, 25, 24, 3, 4, 15]
                        }]
                    },
                    {
                        title: {
                            text: '2012年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [1, 48, 18, 7, 1, 13, 81, 8, 70, 24, 39, 11, 40, 29, 3, 3, 20]
                        }]
                    },
                    {
                        title: {
                            text: '2013年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [3, 53, 19, 6, 5, 11, 75, 19, 85, 27, 52, 16, 53, 34, 6, 2, 17]
                        }]
                    },
                    {
                        title: {
                            text: '2014年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [3, 65, 18, 5, 9, 16, 113, 19, 82, 40, 46, 14, 52, 34, 6, 1, 27]
                        }]
                    },
                    {
                        title: {
                            text: '2015年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [5, 46, 15, 7, 7, 12, 72, 15, 72, 28, 27, 15, 42, 32, 5, 2, 18]
                        }]
                    },
                    {
                        title: {
                            text: '2016年电影类型变化趋势',
                            x: 'center'
                        },
                        series: [{
                            data: [5, 47, 20, 10, 6, 14, 101, 14, 82, 32, 45, 16, 41, 23, 6, 2, 23]
                        }]
                    }
                ]
            },
            options5: {
                title: {
                    x: '44.5%',
                    y: '2%'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data: ['剧情片', '喜剧片', '惊悚片', '动作片', '爱情片', '冒险片', '恐怖片', '家庭片', '奇幻片', '悬疑片', '犯罪片', '科幻片', '历史片', '战争片', '西部片', '动画片', '音乐片', '纪录片']
                },
                series: [{
                        name: '分类方法',
                        type: 'pie',
                        selectedMode: 'single',
                        radius: [0, '30%'],

                        label: {
                            normal: {
                                position: 'inner'
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data: [{
                                value: 9936,
                                name: '情绪'
                            },
                            {
                                value: 1653,
                                name: '场景'
                            },
                            {
                                value: 529,
                                name: '形式'
                            }
                        ]
                    },
                    {
                        name: '影片类型',
                        type: 'pie',
                        radius: ['40%', '75%'],
                        label: {
                            normal: {
                                formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                                backgroundColor: '#eee',
                                borderColor: '#aaa',
                                borderWidth: 1,
                                borderRadius: 4,
                                rich: {
                                    a: {
                                        color: '#999',
                                        lineHeight: 22,
                                        align: 'center'
                                    },
                                    hr: {
                                        borderColor: '#aaa',
                                        width: '100%',
                                        borderWidth: 0.5,
                                        height: 0
                                    },
                                    b: {
                                        fontSize: 11,
                                        lineHeight: 27
                                    },
                                    per: {
                                        color: '#eee',
                                        backgroundColor: '#334455',
                                        padding: [2, 4],
                                        borderRadius: 2
                                    }
                                }
                            }
                        },
                        data: [

                            {
                                value: 894,
                                name: '爱情片'
                            },
                            {
                                value: 519,
                                name: '恐怖片'
                            },
                            {
                                value: 424,
                                name: '奇幻片'
                            },
                            {
                                value: 1274,
                                name: '惊悚片',
                                selected: true
                            },
                            {
                                value: 348,
                                name: '悬疑片'
                            },
                            {
                                value: 696,
                                name: '犯罪片'
                            },
                            {
                                value: 535,
                                name: '科幻片'
                            },
                            {
                                value: 1154,
                                name: '动作片'
                            },
                            {
                                value: 197,
                                name: '历史片'
                            },
                            {
                                value: 790,
                                name: '冒险片'
                            },
                            {
                                value: 144,
                                name: '战争片'
                            },
                            {
                                value: 1722,
                                name: '喜剧片',
                                selected: true
                            },
                            {
                                value: 82,
                                name: '西部片'
                            },
                            {
                                value: 234,
                                name: '动画片'
                            },
                            {
                                value: 185,
                                name: '音乐片'
                            },
                            {
                                value: 513,
                                name: '家庭片'
                            },
                            {
                                value: 2297,
                                name: '剧情片',
                                selected: true
                            },
                            {
                                value: 110,
                                name: '记录片'
                            }
                        ]
                    }
                ]
            }
        }
    },
    mounted: function () {
        var api1 = "http://127.0.0.1:8000/api/test4";
        Axios.get(api1).then((response) => {
            console.log(response.data)
            this.options1.xAxis.data = response.data.list1
            this.options1.series[0].data = response.data.list2
            this.options1.series[1].data = response.data.list3
            this.options1.series[2].data = response.data.list4
            this.options1.series[3].data = response.data.list5
        })

        var api2 = "http://127.0.0.1:8000/api/test5";
        Axios.get(api2).then((response) => {
            this.options2.dataset.source = response.data
        })

        var api3 = "http://127.0.0.1:8000/api/test9";
        Axios.get(api3).then((response) => {
            this.options3.xAxis.data = response.data.list1
            this.options3.series.data = response.data.list2
        })
    }
}
</script>

<style>
.name {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 10px;
}
</style>
