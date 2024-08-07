document.getElementById("TopicForm").onsubmit = function(){
    const Auto = document.getElementById("Auto").checked
    const Manual = document.getElementById("Manual").checked
    const checks = Get_Check_Stats()
    if ((Auto) || (Manual && checks > 0)){
        // Display page based on which condition is true
        return true
    } else {
        return false
    }
}

function Change_Check_State(state) {
    const inputs = document.getElementById("TopicForm").getElementsByTagName("input");
    for (const i of inputs) {
        if (i.type === "checkbox" && i.id !== "Auto" && i.id !== "Manual") {
            i.disabled = state;
            if (i.disabled){
                i.checked = false
            }
        }
    }
}

function Get_Check_Stats() {
    const inputs = document.getElementById("TopicForm").getElementsByTagName("input");
    let states = 0
    for (const i of inputs) {
        if (i.type === "checkbox" && i.id !== "Auto" && i.id !== "Manual" && i.checked) {
            states++
        }
    }
    return states
}


document.getElementById("Manual").onchange = function(){
    if (document.getElementById("Manual").checked){
        Change_Check_State(false)
        document.getElementById("Auto").checked = false
    }
}

document.getElementById("Auto").onchange = function(){
    if (document.getElementById("Auto").checked){
        Change_Check_State(true)
        document.getElementById("Manual").checked = false
    }
}

