<template>
<div style="text-align: center">
    <v-chart :options="options3" style="display: inline-block; margin: 10px auto 10px auto; width: 900px; height: 500px;" />
    <div class="name">电影受欢迎程度与各数据的相关性分析</div>
    <v-chart :options="options5" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options6" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options7" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options8" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
</div>
</template>

<script>
import Axios from 'axios';
export default {
    data() {
        return {        
            options3: {
                title: {
                    text: 'facebook喜欢的人数排名前十五的电影',
                    left: 290,
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    formatter: function (arg) {
                        return arg.name + ' imdb评分：' + arg.data
                    },
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'shadow', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                legend: {},
                xAxis: {
                    name: '电影名',
                    position: 'bottom',
                    offset: 15,
                    nameLocation: 'end',
                    nameTextStyle: {
                        color: "#000",
                        padding: [5, 0, 0, -5],
                    },
                    nameGap: 15,
                    nameRotate: 0,
                    axisLabel: {
                        interval: 0,
                        rotate: '20',
                    },
                    data: []
                },
                yAxis: {
                    name: "人数"
                },
                grid: {
                    show: false, //---是否显示直角坐标系网格
                    top: 80, //---相对位置，top\bottom\left\right  
                    bottom: '30%',
                    tooltip: { //---鼠标焦点放在图形上，产生的提示框
                        show: true,
                        trigger: 'item', //---触发类型
                        textStyle: { //---提示框样式
                            color: '#fff',
                        },
                    }
                }, //位置设置
                series: {
                    type: 'bar',
                    //折线拐点标志的样式 
                    itemStyle: {
                        normal: {
                            color: function (params) {
                                var colorList = ['#d48265', '#61a0a8', '#749f83','#c23531', '#2f4554',  '#91c7ae', '#ca8622'];
                                // var colorList = ['#c23531','#2f4554', '#61a0a8'];
                                // 自动循环已经有的颜色
                                return colorList[params.dataIndex % colorList.length];
                            }
                        }
                    },
                    label: {
                        show: true,
                        position: 'top'
                    },
                    data: []
                }
            },
            options5: {
                title: {
                    text: '与imdb评分'
                },
                xAxis: {
                    name: 'imdb评分'
                },
                yAxis: {
                    name: '人数'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options6: {
                title: {
                    text: '与用户的评论数量'
                },
                xAxis: {
                    name: '评论数'
                },
                yAxis: {
                    name: '人数'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options7: {
                title: {
                    text: '与参与投票的用户数量'
                },
                xAxis: {
                    name: '投票数'
                },
                yAxis: {
                    name: '人数'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options8: {
                title: {
                    text: '与脸书上投喜爱的总数'
                },
                xAxis: {
                    name: '喜爱数'
                },
                yAxis: {
                    name: '人数'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            }
        }
    },
    mounted: function () {
        var api1 = "http://127.0.0.1:8000/api/test12";
        Axios.get(api1).then((response) => {
            console.log(response.data)
            const self = this;
            self.options3.xAxis.data = response.data.list1
            self.options3.series.data = response.data.list2
        })

        var api3 = "http://127.0.0.1:8000/api/test11";
        Axios.get(api3).then((response) => {
            console.log(response.data)
            this.options5.series.data = response.data.list1
            this.options6.series.data = response.data.list2
            this.options7.series.data = response.data.list3
            this.options8.series.data = response.data.list4
        })
    }
}
</script>

<style>

</style>
