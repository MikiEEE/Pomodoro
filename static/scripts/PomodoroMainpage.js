

let timing = 5
let data
let timer = '00:01'

try{
    document.getElementById('timer').innerHTML = timer
}
catch(err){
  console.log(err);
}

function startTimer() {
  var presentTime = document.getElementById('timer').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  var m = timeArray[0];
  var s = checkSecond((timeArray[1] - 1));
  if(s==59){m=m-1}
  if(m<0){
    document.getElementById('timer').innerHTML = timer
    updateTask()
    return
  }

  document.getElementById('timer').innerHTML = m + ":" + s;
  setTimeout(startTimer, 1000);
}

function checkSecond(sec) {
  if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
  if (sec < 0) {sec = "59"};
  return sec;
}

/*
@function setData() - onclick gets element name and sets data to it to
  prepare for the post request
@param item - html object
*/
function setData(item) {
   data = {name:$.trim($(item).attr('name'))}
}

function downloadCSV(){
  console.log('call was made');
  $.ajax({
    method:'GET',
    url:'/downloadPomodoro',
  })
}

function updateTask() {
  if(data){
    console.log('DATA',data);
    $.ajax({
      method:'POST',
      url:'/finishedPomodoro',
      data:JSON.stringify(data),
      contentType: "application/json",
    })
  }
  console.log('done');
}
