document.addEventListener('DOMContentLoaded', function () {
    const ingredients = document.querySelectorAll('.ingredient-item');
    const dropZone = document.querySelector('#drop-zone');

    if (ingredients && dropZone) {
        ingredients.forEach(ingredient => {
            ingredient.addEventListener('dragstart', handleDragStart);
            ingredient.addEventListener('dragend', handleDragEnd);
        });

        dropZone.addEventListener('dragover', handleDragOver);
        dropZone.addEventListener('drop', handleDrop);
    }

    function handleDragStart(e) {
        e.dataTransfer.setData('text/plain', e.target.id);
        e.target.classList.add('dragging');
    }

    function handleDragEnd(e) {
        e.target.classList.remove('dragging');
    }

    function handleDragOver(e) {
        e.preventDefault();
    }

    function handleDrop(e) {
        e.preventDefault();
        const id = e.dataTransfer.getData('text');
        const draggable = document.getElementById(id);
        dropZone.appendChild(draggable);
    }
});
