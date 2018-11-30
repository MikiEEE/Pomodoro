let data
const timer = '25:00'


function initializeTimer(){
  try{
      document.getElementById('timer').innerHTML = timer
  }
  catch(err){
    console.log(err);
  }
  return
}


function startTimer() {
    if(data) {
      var presentTime = document.getElementById('timer').innerHTML;
      var timeArray = presentTime.split(/[:]+/);
      var m = timeArray[0];
      var s = checkSecond((timeArray[1] - 1));
      if(s==59) {
        m=m-1
      }
      if(m<0) {
        document.getElementById('timer').innerHTML = timer
        updateTask()
        alert(`Your Interval is Complete: ${data.name}`)
        return
    }
  }
  else {
    alert('Please Select A Project')
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
   setElement('#SELECTEDPROJECT', $.trim($(item).attr('name')))
}

function setElement(elemID, text) {
  let newText = $(elemID).text().slice(0,18)
  newText += text
  $(elemID).text(newText)
  return
}

function downloadCSV(){
  $.ajax({
    method:'GET',
    url:'/downloadPomodoro',
  })
}

function updateTask() {
  if(data){
    $.ajax({
      method:'POST',
      url:'/finishedPomodoro',
      data:JSON.stringify(data),
      contentType: "application/json",
    })
  }
}

function setSelectedDefault() {
  if(!data && $('#ElementExists').length){
    setData('#ElementExists')
    setElement('#SELECTEDPROJECT',$('#ElementExists').eq(0).attr('name'))
  }
}

setSelectedDefault()
initializeTimer()
