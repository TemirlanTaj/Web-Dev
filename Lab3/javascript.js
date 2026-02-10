const taskForm = document.getElementById('todo_form_id');
const taskInput = document.getElementById('todo-input');
const taskList = document.getElementById('todo-list');

taskForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const newTask = taskInput.value.trim();

    if (newTask === '') {
        return;
    }

    createTask(newTask);

    taskInput.value = '';
});

function createTask(taskContent) {
    const item = document.createElement('li');
    item.className = 'todo_item_class';

    const taskWrapper = document.createElement('div');
    taskWrapper.className = 'todo_left_class';

    const completeCheckbox = document.createElement('input');
    completeCheckbox.type = 'checkbox';

    const taskLabel = document.createElement('span');
    taskLabel.textContent = taskContent;
    taskLabel.className = 'todo_text_class';

    completeCheckbox.addEventListener('change', function () {
        taskLabel.classList.toggle('done');
    });

    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Delete';
    removeBtn.className = 'delete_btn_class';

    removeBtn.addEventListener('click', function () {
        item.remove();
    });

    taskWrapper.appendChild(completeCheckbox);
    taskWrapper.appendChild(taskLabel);

    item.appendChild(taskWrapper);
    item.appendChild(removeBtn);

    taskList.appendChild(item);
}