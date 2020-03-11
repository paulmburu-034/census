
function Death_Census_analysis() {
    $('#theguide').show();
    $.ajax({
        type:"GET",
        url:"/analysis/death_population/",
        dataType:"json",
        async:true,
        data:{ csrfmiddlewaretoken: '{{ csrf_token }}'},
        success:jsonDeathCensus,
        fail: failxml
    });
    $.ajax({
        type:"GET",
        url:"/analysis/death_analysis/",
        dataType:"json",
        async:true,
        data:{ csrfmiddlewaretoken: '{{ csrf_token }}'},
        success:deathJsonCensus,
        fail: failxml
    });


    function jsonDeathCensus(census) {
        $('#theguide').fadeOut();
        var output='<div class="maininfo">';
        var count = census.filter(function(element) {
            return element.pk;
        }).length;
        total_male = 0;
        total_female = 0;
        total_male_per_county = 0;
        total_female_per_county = 0;
        $(census).each(function(key, value){
            $(value.fields).each(function(i, val){

                if (val.gender === 'male') {
                    total_male++;
                }
                else{
                    total_female++;
                }

            });

        });
        output+= '<h4>Total Population: '+count+'</h4>';
        output+= '<h4>Total Male Population: '+total_male+'</h4>';
        output+= '<h4>Total Female Population: '+total_female+'</h4>';
       output+='</div';

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

        $('#output').html(output);
        $("#output").fadeIn(1000);
        google.charts.setOnLoadCallback(drawMaleFemaleChart);
    }
    function failxml() {
        $('#output').html('Sorry! We could not load the crops at the moment');
        $('#theguide').hide();
        }

    function deathJsonCensus(census) {
        var count = census.filter(function(element) {
            return element.pk;
        }).length;
        var year2017 = 0;
        var year2018 = 0;
        var year2019 = 0;
        var previous_years = 0;
        var nairobi_county = 0;
        var kisumu_county = 0;
        var nakuru_county = 0;
        var mombasa_county = 0;
        var nyeri_county = 0;
        var uasin_gishu_county = 0;
        var baringo_county = 0;
        var narok_county = 0;
        var other_counties = 0;
        $(census).each(function(key, value){
            $(value.fields).each(function(i, val){
                var date = new Date(val.death_reg_date);
                var day  = date.getDate();
                var mnth = date.getMonth();
                var year = date.getFullYear();
                var hrs  = date.getHours();
                var mnts = date.getMinutes();
                if (year===2017){
                    year2017++;
                }
                else if(year===2018){
                    year2018++;
                }
                else if(year===2019){
                    year2019++;
                }
                else{
                    previous_years++;
                }

                if (val.current_county === 'nairobi') {
                    nairobi_county++;
                }
                else if (val.current_county === 'kisumu') {
                    kisumu_county++;
                }
                else if (val.current_county === 'nakuru') {
                    nakuru_county++;
                }
                else if (val.current_county === 'mombasa') {
                    mombasa_county++;
                }
                else if (val.current_county === 'nyeri') {
                    nyeri_county++;
                }
                else if (val.current_county === 'uasin gishu') {
                    uasin_gishu_county++;
                }
                else if (val.current_county === 'baringo') {
                    baringo_county++;
                }
                else if (val.current_county === 'narok') {
                    narok_county++;
                }
                else{
                    other_counties++;
                }

            });

        });
       function drawChart() {
            // Define the chart to be drawn.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Death Population per year');
            data.addColumn('number', 'Percentage');
            data.addRows([
               ['2017', year2017],
               ['2018', year2018],
               ['2019', year2019],
               ['Previous years', previous_years],
            ]);
            var options = {'title':'Death Population percentage for three years', 'width':750, 'height':400};
            var chart = new google.visualization.PieChart(document.getElementById ('pie'));
            chart.draw(data, options);
         }
         function drawCountyChart() {
            // Define the chart to be drawn.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Death Population for Counties');
            data.addColumn('number', 'Percentage');
            data.addRows([
               ['Nairobi', nairobi_county],
               ['Kisumu', kisumu_county],
               ['Nakuru', nakuru_county],
               ['Mombasa', mombasa_county],
               ['Nyeri', nyeri_county],
               ['Uasin Gishu', uasin_gishu_county],
               ['Baringo', baringo_county],
               ['Narok', narok_county],

            ]);
            var options = {'title':'Death Population percentage for Counties', 'width':750, 'height':400};
            var chart = new google.visualization.PieChart(document.getElementById ('counties'));
            chart.draw(data, options);
         }
         function drawCountyMaleFemaleChart() {
            // Define the chart to be drawn.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Name of the county');
            data.addColumn('number', 'Total Death Population');
            data.addRows([
               ['Nairobi', nairobi_county ],
               ['Kisumu', kisumu_county ],
               ['Nakuru', nakuru_county ],
               ['Mombasa', mombasa_county ],
               ['Nyeri', nyeri_county ],
               ['Uasin Gishu', uasin_gishu_county ],
               ['Baringo', baringo_county ],
               ['Narok', narok_county ]

            ]);

            var options = {
               showRowNumber: true,
               width: '700%',
               height: '40%'
            };

            // Instantiate and draw the chart.
            var chart = new google.visualization.Table(document.getElementById('pop_per_counties'));
            chart.draw(data, options);
         }
        google.charts.setOnLoadCallback(drawChart);
        google.charts.setOnLoadCallback(drawCountyChart);
        google.charts.setOnLoadCallback(drawCountyMaleFemaleChart);
    }

 }
