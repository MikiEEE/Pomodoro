

let timing = 5
let data

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
    url:'/downloadPomodoro',
  })
}

console.log('LENGTH:',$('#navbarElements').length)

$('#test').click(function(){
  //data = {name:$.trim($('#selectedTask option:selected').text())}
  console.log('DATA',data);
  $.ajax({
    method:'POST',
    url:'/finishedPomodoro',
    data:JSON.stringify(data),
    contentType: "application/json",
  })
  console.log('done');
})
