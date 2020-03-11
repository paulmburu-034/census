
        function drawMaleFemaleChart() {
            // Define the chart to be drawn.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Population for Male and Female');
            data.addColumn('number', 'Percentage');
            data.addRows([
               ['Male', total_male],
               ['Female', total_female],

            ]);
            var options = {'title':'Population percentage for Male and Female', 'width':550, 'height':400};
            var chart = new google.visualization.PieChart(document.getElementById ('male_female'));
            chart.draw(data, options);
         }

        google.charts.setOnLoadCallback(drawMaleFemaleChart);