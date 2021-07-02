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



//마커포스팅이미지 테스트 코드

var imageSrc = '../../static/images/test_marker.png', // 마커이미지의 주소입니다    
    imageSize = new kakao.maps.Size(50, 50), // 마커이미지의 크기입니다
    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

// 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
    markerPosition = new kakao.maps.LatLng(37.44875, 127.286619); // 마커가 표시될 위치입니다

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
  position: markerPosition,
  image: markerImage // 마커이미지 설정 
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);  



//커스텀 오버레이로 포스팅이미지 나열해보기
//마커용 오버레이에 들어갈 내용
var test_content = '<div class="test_overlaybox">' +
    '   <div class="box_header">' + //오버레이 윗부분
    '        <div class="title">' +
    '           <span class="marker">' +
    '               <img src="../../static/images/logpage_marker.png" >' +
    '           </span>'+
    '           <span>' +
    '               <div class="close" onclick="closeOverlay()" title="닫기">'+
    '                   <img src="https://cdn.pixabay.com/photo/2016/10/10/01/49/x-1727490_960_720.png"'+
    '               </div>' + 
    '           </span>' +
    '        </div>' + 
    '   </div>' +   
    '   <div class="imageBox">' + //오버레이 본문부분
    '       <div class = "imageBox_Title">' + //사진 윗부분
    '           PHOTO' +
    '       </div>' +
    '       <div class = "Images">' + //갤러리가 될 부분
    '           <ul class="Image">'+
    '               <li>' + '<img src="https://images.unsplash.com/photo-1611601184963-9d1de9b79ff3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80">' + '</li>' +
    '               <li>' + '<img src="https://images.unsplash.com/photo-1618427012166-b0e03d490a4a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80">' + '</li>' +
    '               <li>' + '<img src="https://images.unsplash.com/photo-1573164574472-797cdf4a583a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80">' + '</li>' +
    '               <li>' + '<img src="https://images.unsplash.com/photo-1595574987326-6bf754c09257?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80">' + '</li>' +
    '               <li>' + '<img src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=727&q=80">' + '</li>' +
    '               <li>' + '<img src="https://images.unsplash.com/photo-1612160609504-334bdc6b70c9?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80">' + '</li>' +
    '           </ul>' +
    '       </div>' +
    '   </div>' +
    '   <div class = "buttons">' + //스크롤 버튼이 될 부분
    '           <span>' + //아래 스크롤 버튼
    '               <div class="btn" onclick="" title="아래스크롤">' +
    '                   <img src="../../static/images/scroll_btn1.png"' +
    '               </div>' + 
    '           </span>' +
    '           <span>' + //위 스크롤 버튼
    '               <div class="btn" onclick="" title="위스크롤">' +
    '                   <img src="../../static/images/scroll_btn2.png"' +
    '               </div>' + 
    '           </span>' +
    '   </div>' +
    '</div>';
    

//마커용 오버레이 나타내기
var test_overlay = new kakao.maps.CustomOverlay({
    content: test_content,
    position: marker.getPosition()
});

//마커 클릭 시 오버레이 나타나도록하기
kakao.maps.event.addListener(marker, 'click', function(){
    test_overlay.setMap(map);
});

//닫기(X)버튼을 눌렀을 때 오버레이 사라지도록
function closeOverlay() {
    test_overlay.setMap(null);     
}

