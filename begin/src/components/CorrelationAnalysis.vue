<template>
<div>
    <!-- <div class="name">电影各数据的相关性分析</div> -->
    <v-chart :options="options1" style="display: inline-block; margin: 20px 150px; width: 1000px; height: 800px;" />
</div>
</template>

<script>
import Axios from 'axios';
export default {
    data() {
        return {
            options1: {
                title: {
                    text: "电影各数据的相关性分析",
                    left: 440
                },
                tooltip: {
                    position: 'top'
                },
                grid: {
                    height: '50%',
                    top: '10%',
                    left: "260px",
                    right: "20%"
                },
                xAxis: {
                    type: 'category',
                    data: [],
                    splitArea: {
                        show: true
                    },
                    axisLabel: {
                        interval: 0,
                        rotate: '90'
                    },
                },
                yAxis: {
                    type: 'category',
                    data: [],
                    splitArea: {
                        show: true,
                    },
                    axisLabel: {
                        interval: 0,
                    },
                },
                visualMap: {
                    min: -0.13227353591161753,
                    max: 1,
                    calculable: true,
                    orient: 'horizontal',
                    left: 'center',
                    bottom: '15%'
                },
                series: {
                    name: '',
                    type: 'heatmap',
                    data: [],
                    label: {
                        show: false
                    },
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            }
        }
    },
    mounted: function () {
        var api1 = "http://127.0.0.1:8000/api/test8";
        Axios.get(api1).then((response) => {
            this.options1.xAxis.data = response.data.list1
            this.options1.yAxis.data = response.data.list1
            this.options1.series.data = response.data.list2
        })
    }
}
</script>

<style>

</style>
