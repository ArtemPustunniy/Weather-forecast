const load = document.getElementById('load_main');
const first = document.getElementsByClassName('first')[0];
const second = document.getElementsByClassName('second')[0];


function geo(){

    load.hidden = false;
    first.hidden = true;
    second.hidden = true;

    navigator.geolocation.getCurrentPosition(function(position) {
// Геопозиция доступна
        var lat = position.coords.latitude;
        console.log(lat);
        var lon = position.coords.longitude;
        console.log(lon);
//        const key = '5aa741a37ff6512516bcb3da3ea973f0';
        const key = '27821183e572d2b9e8d7280cd47273d1';
        var url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&units=metric&lang=en&appid=' + key;

        get(url);

    }, function (positionError){
// Геопозиция НЕ доступна
        if (GeolocationPositionError.PERMISSION_DENIED){

            const key = '5aa741a37ff6512516bcb3da3ea973f0';
            var url = 'http://api.openweathermap.org/data/2.5/weather?q=Санкт-Петербург&units=metric&lang=en&appid=' + key;
//            var url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + '59.852' + '&lon=' + '30.153' + '&units=metric&lang=en&appid=' + key;
            get(url);
        }
    })

}


geo()

function get(url){
    fetch(url).then(function (resp) {return resp.json() }).then(function (data) {
        document.querySelector(".first h2").textContent = data.name;
        document.querySelector('.weather__icon').innerHTML = `<img src="http://openweathermap.org/img/wn/${data.weather[0]['icon']}@2x.png">`;
        document.querySelector(".first p").textContent = data.main.temp + '°C';

        document.querySelector(".wind").textContent = data.wind.speed + ' m/s';
        document.querySelector(".cloud").textContent = data.clouds.all + '%';
        document.querySelector(".pressure").textContent = data.main.pressure + ' hpa';
        document.querySelector(".humidity").textContent = data.main.humidity +'%';
        document.querySelector(".coord").textContent = '['+data.coord.lat + ', ' + data.coord.lon + ']';


        load.hidden = true;
        first.hidden = false;
        second.hidden = false;
    })
        // Обработка ошибок
        .catch(function () {
            //Обрабатываем ошибки
            alert("Ошибка запроса");
        });

}

update_desktop = document.getElementById('button-desktop');
update_mobile= document.getElementById('button-mobile');
update_desktop.addEventListener("click", geo);
update_mobile.addEventListener("click", geo);