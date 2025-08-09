// static/script.js
(() => {
  const slotsEl = document.getElementById('slots');
  const addBtn = document.getElementById('addBtn');
  const removeBtn = document.getElementById('removeBtn');

  function createSlot() {
    const idx = slotsEl.children.length;
    const card = document.createElement('div');
    card.className = 'slot-card';
    card.innerHTML = `
      <div class="slot-header"><strong>Competitor ${idx + 1}</strong></div>
      <div class="slot-body">
        <div class="preview-wrap"><img class="preview" src="" hidden></div>
        <div class="inputs">
          <label class="file-label">
            <input type="file" accept="image/*" name="images" class="file-input">
            <span class="file-btn">Choose Image</span>
          </label>
          <input type="text" name="names" class="text-input" placeholder="Fish name (optional)">
        </div>
      </div>
      <div class="slot-footer"><button type="button" class="remove-this">Remove</button></div>
    `;

    const fileInput = card.querySelector('.file-input');
    const preview = card.querySelector('.preview');
    const removeBtnLocal = card.querySelector('.remove-this');

    fileInput.addEventListener('change', (e) => {
      const f = e.target.files && e.target.files[0];
      if (!f) {
        preview.hidden = true;
        preview.src = '';
        return;
      }
      const reader = new FileReader();
      reader.onload = (ev) => {
        preview.src = ev.target.result;
        preview.hidden = false;
      };
      reader.readAsDataURL(f);
    });

    removeBtnLocal.addEventListener('click', () => {
      card.remove();
      renumber();
    });

    slotsEl.appendChild(card);
    renumber();
  }

  function renumber() {
    Array.from(slotsEl.children).forEach((c, i) => {
      const strong = c.querySelector('.slot-header strong');
      if (strong) strong.textContent = `Competitor ${i + 1}`;
    });
  }

  // Create initial 4 slots
  for (let i = 0; i < 4; i++) createSlot();

  addBtn.addEventListener('click', createSlot);
  removeBtn.addEventListener('click', () => {
    if (slotsEl.lastElementChild) {
      slotsEl.lastElementChild.remove();
      renumber();
    }
  });
})();
