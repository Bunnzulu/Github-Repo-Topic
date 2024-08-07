document.getElementById("TopicForm").onsubmit = function(){
    // for (const i of document.getElementById("TopicForm").getElementsByTagName("input")) {
    //     console.log(i)
    //     console.log(i.checked)
    // }

    return false
}

function Disable_Boxes(state) {
    for (const i of document.getElementById("TopicForm").getElementsByTagName("input")) {
        if (i.id in ("Auto","Manual",""))
        console.log(i.checked)
} }



document.getElementById("Manual").onchange = function(){
    if (document.getElementById("Manual").checked){
        console.log()
    }
}