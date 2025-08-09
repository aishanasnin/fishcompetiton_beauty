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
      <div class="slot-header"><strong>Competitor ${idx+1}</strong></div>
      <div class="slot-body">
        <div class="preview-wrap"><img class="preview" src="" hidden></div>
        <div class="inputs">
          <label class="file-label">
            <input type="file" accept="image/*" name="images" class="file-input">
            <span class="file-btn">Choose Image</span>
          </label>
          <input type="text" name="names" class="text-input" placeholder="Fish name (optional)">
