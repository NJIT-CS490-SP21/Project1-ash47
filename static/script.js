//alert('Hello world!');
function sendReq(song_name, artist_name, song_image, song_audio, artist_list)
{
    const url = '/lyrics/' + song_name + '/' + artist_name;
    window.fetch(url).then(response => response.json()) 
        .then(data => { 
            console.log(data);
            
            let lyrics_box = document.getElementById("lyrics_box");
            
            let text = document.getElementById("text");
            text.innerHTML = data['Lyrics'];
            
            let songImage = document.getElementById("image_box");
            songImage.src = song_image;
            
            let songName = document.getElementById("song_box");
            songName.innerHTML = song_name;
            
            
            let artist_box = document.getElementById("artist_box");
            artist_box.innerHTML = artist_list;
            
            let audioControl = document.getElementById('control');
            let songAudio = document.getElementById("audio_box");
            songAudio.src =  song_audio;
            songAudio.type = 'audio/ogg';
            audioControl.load();
            
            let background = document.getElementById("lyrics_bg");
            background.style.filter = "blur(5px)";
            
            hideLoader();
            lyrics_box.style.display = 'grid';
        });
        
}

function showLoader()
{
    var loader = document.getElementById("loader");
    loader.style.display = "block";
}
function hideLoader()
{
    var loader = document.getElementById("loader");
    loader.style.display = "none";
}

window.onload = () => { 
    
    document.getElementById('tabf0').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name0").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image0").src;
        var song_audio = document.getElementById("audio0").src;
        var artist_list = document.getElementById("name_list0").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    
    document.getElementById('tabf1').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name1").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image1").src;
        var song_audio = document.getElementById("audio1").src;
        var artist_list = document.getElementById("name_list1").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf2').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name2").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image2").src;
        var song_audio = document.getElementById("audio2").src;
        var artist_list = document.getElementById("name_list2").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf3').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name3").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image3").src;
        var song_audio = document.getElementById("audio3").src;
        var artist_list = document.getElementById("name_list3").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf4').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name4").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image4").src;
        var song_audio = document.getElementById("audio4").src;
        var artist_list = document.getElementById("name_list4").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf5').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name5").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image5").src;
        var song_audio = document.getElementById("audio5").src;
        var artist_list = document.getElementById("name_list5").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf6').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name6").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image6").src;
        var song_audio = document.getElementById("audio6").src;
        var artist_list = document.getElementById("name_list6").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf7').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name7").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image7").src;
        var song_audio = document.getElementById("audio7").src;
        var artist_list = document.getElementById("name_list7").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf8').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name8").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image8").src;
        var song_audio = document.getElementById("audio8").src;
        var artist_list = document.getElementById("name_list8").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    document.getElementById('tabf9').addEventListener('click', () => {
        console.log('Button was clicked!');
        
        var song_name = document.getElementById("name9").innerHTML;
        var artist_name = document.getElementById("artist_name").innerHTML;
        var song_image = document.getElementById("image9").src;
        var song_audio = document.getElementById("audio9").src;
        var artist_list = document.getElementById("name_list9").innerHTML;
        
        showLoader();
        sendReq(song_name, artist_name, song_image, song_audio, artist_list);
        
    });
    
    var closebtns = document.getElementById("close");

      closebtns.addEventListener("click", function() {
        this.parentElement.style.display = 'none';
        let background = document.getElementById("lyrics_bg");
            background.style.filter = 'none';
      });
    
};
