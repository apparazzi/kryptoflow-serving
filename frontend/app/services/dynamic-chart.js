import { copy } from '@ember/object/internals';
import Service from '@ember/service';


export default Service.extend({

  getRandomInt(min, max) {
    return parseInt(Math.random() * (max - min) + min, 10);
  },

  updateSeriesData(chartData, rangeStart, rangeEnd) {
    let numPoints = this.getRandomInt(rangeStart, rangeEnd);
    return chartData.map((series) => {
      return {
        name: series.name,
        data: series.data.slice(0, numPoints)
      };
    });
  },

  updateSeriesCount(chartData, numSeries) {
    let chartDataCopy = copy(chartData, true);
    return chartDataCopy.slice(0, numSeries);
  },

  addDataPoint(chartData, point) {
    console.log(point, 'PRICES');
    chartData.addPoint(point.price, true)
  }
});

