function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(53.344435, -6.264790),
        zoom: 14,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(53.344435, -6.264790),
        animation: google.maps.Animation.BOUNCE
    });

    marker.setMap(map);
}