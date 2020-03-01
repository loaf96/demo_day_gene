function buildCharts() {
  

    var randReturns = [];
    var eventTypes = {
    
      x : ['CPI', 'Retail Sales', 'Trade Balance', 'Industrial Production', 'PPI', 'GDP', 'Unemployment Rate', 'Manufacturing PMI', 'Core CPI', 'Imports'],
      y: [2566, 1894, 1690, 1656, 1553, 1381, 1149, 1028, 996, 784]
      
  };

    var countryinfo = {

      x : ['Australia',
      'Brazil',
      'Canada',
      'China',
      'Euro Zone',
      'France',
      'Germany',
      'Hong Kong',
      'India',
      'Italy',
      'Japan',
      'New Zealand',
      'Russia',
      'Singapore',
      'South Africa',
      'South Korea',
      'Spain',
      'Switzerland',
      'United Kingdom',
      'United States'],

    y: [5070,  3409,  4564,  2055,  5829,  3726,  4306,   960,  2735, 3354,  7343,  3894,  2086,  1340,  2214,  2403,  2362,  2240, 7802, 28817]
    };
  
    // var trace1 = {
    //   values: countryinfo.y,
    //   labels: countryinfo.x,
    //   hovertext: countryinfo.x,
    //   type: 'pie'
    // };

      // var trace2 = {
      //   x: time,  //FUCKING SHIT
      //   y: randReturns,
      //   mode: 'markers',
      //   marker: {
      //     size: eventCountbyDay,
      //   },
      // };

    
      var trace3 = {
        x: eventTypes.x,
        y: eventTypes.y,
        text: eventTypes.x,
        name: "Frequency of Events by Type",
        type: "bar",
      };
  
    //   var data1 = [trace1];
      // var data2 = [trace2];
      var data3 = [trace3];
  
    //   var layout1 = {
    //     height: 800,
    //     width: 800,
    //   };
  
      // var layout2 = {
      //   width: 1200,
      //   height: 500
      // };

      var layout3 = {
        width: 1200,
        height: 500
      };
      // var viz1 = d3.select('#visual1')
    //   Plotly.newPlot('visual1', data1, layout1);
      // Plotly.newPlot('visual2', data2, layout2);
      Plotly.newPlot('visual3', data3, layout3);
    };
  function init() {
    buildCharts();
    //Plotly.plot('visual1', data1, layout1);
  }
  init();