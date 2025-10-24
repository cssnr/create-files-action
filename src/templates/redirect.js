// JS

let totalSeconds = Number.parseInt('{{ timer }}')
let targetLocation = '{{ url }}'

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded:', totalSeconds, targetLocation)

    if (totalSeconds === 0) {
        window.location = targetLocation
        return
    }

    const span = document.getElementById('timer')
    // const pad = totalSeconds.toString().length
    totalSeconds--
    const interval = setInterval(() => {
        console.log('totalSeconds:', totalSeconds)
        // span.textContent = totalSeconds.toString().padStart(pad, '0')
        span.textContent = totalSeconds.toString()
        if (totalSeconds === 0) {
            clearInterval(interval)
            window.location = targetLocation
        }
        totalSeconds--
    }, 1000)
})
