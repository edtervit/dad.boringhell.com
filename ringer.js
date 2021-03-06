const alarmSound = document.getElementById('alarm')


function checkIfChecked(ele){
    var id = ele.id;
    
    let checkBox = document.getElementById(id);
    
    
    const alarmSound = document.getElementById('alarm');
        
    const loc = document.getElementById(id)
    
    if (checkBox.checked == true){
        function addZero(i) {
            if (i < 10) {
              i = "0" + i;
            }
            return i;
          }
        
        
        var today = new Date();
        var raceTime = id.slice(id.length - 5);
        var currentTime = addZero(today.getHours()) + ":" + addZero(today.getMinutes());



        console.log(currentTime)
        console.log(raceTime)


        var raceTimeHours = Number(raceTime.slice(0,2))
        var currentTimeHours = Number(currentTime.slice(0,2))

        var raceTimeMinutes = Number(raceTime.slice(3,5))
        var currentTimeMinutes = Number(currentTime.slice(3,5))

        var diffHours = raceTimeHours - currentTimeHours
        var diffMinutes = raceTimeMinutes - currentTimeMinutes

        console.log("Diff hours = " + diffHours)
        console.log("Diff minutes = " + diffMinutes)

        if (diffHours < 0 ){
            alert("Sorry but you've already missed this race.")
            document.getElementById(id).checked = false;
            return
        }
        else if (diffHours === 0 && diffMinutes < 0 ){
            alert("Sorry but you've already missed this race.")
            document.getElementById(id).checked = false;
            return
        }
        

        var totalDiffMinutes = (diffHours * 60) + diffMinutes;
        var totalDiffMilli = totalDiffMinutes * 60000;
        var waitTime = totalDiffMilli - 180000;

        console.log(waitTime)
        if (isNaN(waitTime)){
            alert("error")
            return
        }

        console.log("I'm going to wait: "+  waitTime / 60000 + " minutes.")


        alarmSound.currentTime = 0;
        ringAlarm = setTimeout(function(){
            alarmSound.play()
            document.getElementById(id).parentElement.style.border = "solid 3px tomato"
        }, waitTime);

        

        loc.nextSibling.innerHTML = ` ${waitTime / 60000} minutes until race. `

        let countdownTime = waitTime

        countdown = setInterval(function(){
            console.log(countdownTime)
            countdownTime -= 60000
            console.log("after 6 seconds" + countdownTime)
            if (countdownTime == 0){
                loc.nextSibling.innerHTML = ""
                clearInterval(countdown);
                return
            }
            loc.nextSibling.innerHTML = `${countdownTime / 60000} minutes until race.`
        }
        ,60000)


    }
    else{
        document.getElementById(id).parentElement.style.border = "none";
        alarmSound.pause();
        clearTimeout(ringAlarm);
        clearInterval(countdown);
        loc.nextSibling.innerHTML = ""
        console.log("Clearing alarm");
    }
}

