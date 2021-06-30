var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.502, 127.026581), // 지도의 중심좌표
        level: 10 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 커스텀 오버레이에 표시할 내용입니다     
// HTML 문자열 또는 Dom Element 입니다 
var content = '<div class="overlaybox">' +
    `    <img src="../../static/images/marker_ex.png">` +
    '  </div>';

// 커스텀 오버레이가 표시될 위치입니다
// 아이디어톤 - 임시 마커
var position = [
    new kakao.maps.LatLng(37.51332036170739, 127.10014089376925),
    new kakao.maps.LatLng(37.22187253030484, 127.18661951180192),
    new kakao.maps.LatLng(37.76033162822751, 127.0764170077906),
    new kakao.maps.LatLng(37.44875057945972, 126.45107867359248),
    new kakao.maps.LatLng(37.79340558796354, 127.5244481263201),
    new kakao.maps.LatLng(37.58339973306273, 128.3256722978949),
    new kakao.maps.LatLng(37.55883386958059, 126.80292857780141),
]  

for(var i = 0; i < position.length; i++) {
    // 커스텀 오버레이를 생성합니다
    var customOverlay = new kakao.maps.CustomOverlay({
        position: position[i],
        content: content,
    });

    // 커스텀 오버레이를 지도에 표시합니다
    customOverlay.setMap(map);
}

