

let timing = 5
let data


function setData(item) {
   data = {name:$.trim($(item).attr('name'))}
}
// Array.from('#navbarElements').forEach(function(element) {
//   element.addEventListener('click', function(){
//     data = {name:$.trim($(this).attr('name'))}
//     console.log('THIS:',this);
//     console.log('DATA',data)
//   });
// });


// $('#navbarElements').on('click',function(){
  // data = {name:$.trim($(this).attr('name'))}
  // console.log('THIS:',this);
  // console.log('DATA',data)
// });

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

function progressBar() {
  console.log('outside');
  incrementProgress(0)
  return
}

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
