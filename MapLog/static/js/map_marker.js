var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.502, 127.026581), // 지도의 중심좌표
        level: 50 // 지도의 확대 레벨
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
    new kakao.maps.LatLng(37.77316425787717, 128.94725588570472),
    new kakao.maps.LatLng(35.15317692666829, 129.11865457954067),
    new kakao.maps.LatLng(33.252624335746745, 126.41435869540499),
    new kakao.maps.LatLng(36.37217758681988, 127.3603859967918),
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

