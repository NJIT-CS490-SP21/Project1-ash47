//alert('Hello world!');
function sendReq(song_name, artist_name)
{
    const url = '/lyrics/' + song_name + '/' + artist_name; // This should remind you of APIs in Python!
    alert(url);
    window.fetch(url).then(response => response.json()) // So should JSON conversion!
        .then(data => { // .then will only run the function *once* the data is fetched from the internet
            console.log(data); // See what this logs!
            
            let lyrics_box = document.getElementById("lyrics_box");
            
            lyrics_box.innerHTML = data['Lyrics'];
        });
        
}


window.onload = () => { 
    
    document.getElementById('tabf0').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name0").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    
    document.getElementById('tabf1').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name1").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf2').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name2").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf3').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name3").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf4').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name4").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf5').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name5").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf6').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name6").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf7').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name7").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf8').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name8").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
    document.getElementById('tabf9').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name9").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        sendReq(song_name, artist_name);
        
    });
};
