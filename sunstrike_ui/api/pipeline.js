export async function getPipelines() {
    const res = await fetch(`http://localhost:8080/pipeline`)
    return res.json()
}
