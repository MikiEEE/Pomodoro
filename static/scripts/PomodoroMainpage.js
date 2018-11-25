

let timing = 5

function progressBar() {
  console.log('outside');
  incrementProgress(0)
  return
}
$('#test').click(function(){
  let data = {name:$.trim($('#selectedTask option:selected').text())}
  console.log(data);
$.ajax({
  method:'POST',
  url:'/finishedPomodoro',
  data:JSON.stringify(data),
  contentType: "application/json",
})
console.log('done');
})

function incrementProgress(width) {
  console.log('inside');
  // if(width < 100) {
  //   width = width + 100/timing
  //   document.getElementById("mybar").style.width = width + '%'
  //   console.log("WIDTH:",width)
  //   setTimeout(incrementProgress(width),1000)
  // }
  // if (width == 100) {
  //   $.postJSON('/finishedPomodoro',{$('select[name='selectedTask']').val()})
  //   console.log("request made");
  // }
}
