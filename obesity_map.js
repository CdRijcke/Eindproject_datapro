var map = new Datamap({
        scope: 'world',
        // get container to fill map with
        element: document.getElementById('infomap'),
        projection: 'mercator',
        height: document.getElementById('infomap').clientHeight,
        // for legenda use only
        fills: {
          defaultFill: 'black',
          "< 2.000.000" : '#ffffa0',
          "2.000.000 - 3.000.000" : "#fed976",
          " 3.000.000 - 4.000.000" : "#feb24c",
          "4.000.000 - 6.000.000" : "#fd8d3c",
          "6.000.000 - 8.000.000" : '#fc4e2a',
          "8.000.000- 20.000.000" : '#e31a1c',
          "> 20.000.000" : "#b10026"
        },

        // Data is kept empty for now
        data: {
        }

        })

d3.json("obesity_data.json", function(datas) {
    console.log(datas.fact[1].Value)
})