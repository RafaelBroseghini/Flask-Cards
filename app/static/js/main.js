$('.corner')
  .popup()
;

$('.ui.dropdown')
  .dropdown()
;

function showModal(el) {
  $('.ui.long.modal', function(){
    let card = $(el).parent().parent().parent(),
    topic = card.find(".topic").text(),
    question = card.find(".question").text(),
    modaltitle = document.querySelector(".modaltitle")

    console.log(card);
    console.log(topic);
    console.log(question);
    // console.log();
    // console.log();
    
    
    modaltitle.textContent = topic;
    console.log(modaltitle.textContent);

    $(".highlight").remove();
    $(".modalcontent").append(question)
  })
  .modal('show');
}


