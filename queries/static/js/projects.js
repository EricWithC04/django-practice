document.addEventListener("DOMContentLoaded", (_evento) => {
    const projects = Array.from(document.getElementsByClassName("btn-project"))
    
    projects.forEach(p => {
        p.addEventListener("click", (_e) => {
            window.location.href = `/project/${p.id}`
        })
    })

})
