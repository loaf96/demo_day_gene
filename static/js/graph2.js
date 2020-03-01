function buildCharts() {

var trace1 = {
    x: ['the',
    'i',
    'you',
    'a',
    'and',
    'to',
    'my',
    'in',
    "i'm",
    'it',
    'that',
    'me',
    'on',
    'like',
    'your',
    'with',
    'we',
    'of',
    'got',
    'for',
    'all',
    "don't",
    'just',
    'up',
    'they',
    'get',
    'is',
    'but',
    'this'],
    y: [7837,
        6879,
        5320,
        4853,
        4230,
        4145,
        3385,
        2727,
        2569,
        2423,
        2254,
        2243,
        2167,
        1915,
        1606,
        1550,
        1514,
        1491,
        1482,
        1418,
        1340,
        1291,
        1276,
        1274,
        1211,
        1188,
        1187,
        1171,
        1152],
    type: 'bar',
    name: 'Rap Songs',
  };

  var trace2 = {
    x: ['the',
    'of',
    'to',
    'a',
    'in',
    'and',
    'is',
    'that',
    'dream',
    'which',
    'as',
    '',
    'I',
    'by',
    'it',
    'for',
    'this',
    'with',
    'be',
    'have',
    'are',
    'from',
    'we',
    'not',
    'The',
    'was',
    'an',
    'one',
    'but'],
    y: [3710,
        2235,
        1318,
        947,
        932,
        800,
        712,
        614,
        547,
        540,
        450,
        420,
        386,
        368,
        350,
        335,
        322,
        311,
        306,
        295,
        284,
        280,
        275,
        271,
        240,
        200,
        191,
        184,
        180],
    type: 'bar',
    name: 'Freud',
    xaxis: 'x2',
  yaxis: 'y2',
  };

  // var trace3 = {
  //   x = [],
  //   y = [],
  //   type: 'scatter',
  //   name: 'Alice in Wonderland',
  // };

  // var trace4 = {
  //   x = [],
  //   y = [],
  //   type: 'scatter',
  //   name: 'Freud',
  // };
  
  var data = [trace1, trace2];

  var layout = {

    grid: {rows: 2, columns: 1, pattern: 'independent'},

    title: {
      text:'Word Distribution',
    },
    xaxis: {
      title: {
        text: 'Words',
      },
    },
    yaxis: {
      title: {
        text: 'Word Count',
      }
    },
  };
  
  // Plotly.newPlot('test', data1, layout);
  Plotly.newPlot('bar', data, layout);
  // Plotly.newPlot('scatter', data, layout);

  
};

function init() {
  
      // Use the first sample from the list to build the initial plots
      buildCharts();
    };

  
  // Initialize the dashboard
  init();
  