<template>
<div style="text-align: center">
    <v-chart :options="options1" style="display: inline-block; margin: 10px auto 10px auto; width: 900px; height: 400px;"  />
    <v-chart :options="options2" style="display: inline-block; margin: 10px auto 40px auto; width: 900px; height: 500px;" />
    <!-- <div class="summary">由此可见，美国出品电影数量占比最多，几乎占领了国际上电影的一大部分</div> -->
</div>
</template>

<script>
import Axios from 'axios';
export default {
    data() {
        return {
            options1: {
                title: {
                    text: '电影出品数量前十的国家',
                    left: 370,
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    formatter: function (arg) {
                        return arg.name + ' 电影出品数量：' + arg.data
                    },
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'shadow', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    },
                },
                legend: {},
                xAxis: {
                    name: '国家',
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
                        rotate: '15',
                    },
                    data: []
                },
                yAxis: {
                    name: "数量"
                },
                grid: {
                    show: false,
                    top: 80,
                    bottom: '30%',
                    tooltip: {
                        show: true,
                        trigger: 'item',
                        textStyle: {
                            color: '#fff',
                        },
                    }
                },
                series: {
                    type: 'bar',
                    itemStyle: {
                        normal: {
                            color: function (params) {
                                var colorList = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622'];
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
            options2: {
                title: {
                    text: 'IMDB评分前十五的电影',
                    left: 360,
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
                    name: "分数"
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
            }
        }
    },
    mounted: function () {
        var api1 = "http://127.0.0.1:8000/api/test1";
        Axios.get(api1).then((response) => {
            console.log(response.data)
            const self = this;
            self.options1.xAxis.data = response.data.list1
            self.options1.series.data = response.data.list2
        })
        var api2 = "http://127.0.0.1:8000/api/test2";
        Axios.get(api2).then((response) => {
            console.log(response.data)
            const self = this;
            self.options2.xAxis.data = response.data.list1
            self.options2.series.data = response.data.list2
        })
    }
}
</script>

<style>

.summary {
    text-align: center;
    font-size: 18px;
    /* font-weight: bold; */
    /* margin-top: 50px; */
}
.name {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
