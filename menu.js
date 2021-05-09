function getSelectMenu(label, options) {
  let menuHTML = `
    <div class="mdc-select mdc-select--outlined demo-width-class">
      <div class="mdc-select__anchor" aria-labelledby="outlined-select-label">
        <span class="mdc-notched-outline">
          <span class="mdc-notched-outline__leading"></span>
          <span class="mdc-notched-outline__notch">
            <span id="outlined-select-label" class="mdc-floating-label">${label}</span>
          </span>
          <span class="mdc-notched-outline__trailing"></span>
        </span>
        <span class="mdc-select__selected-text-container">
          <span id="demo-selected-text" class="mdc-select__selected-text"></span>
        </span>
        <span class="mdc-select__dropdown-icon">
          <svg class="mdc-select__dropdown-icon-graphic" viewBox="7 10 10 5" focusable="false">
            <polygon class="mdc-select__dropdown-icon-inactive" stroke="none" fill-rule="evenodd"
              points="7 10 12 15 17 10">
            </polygon>
            <polygon class="mdc-select__dropdown-icon-active" stroke="none" fill-rule="evenodd"
              points="7 15 12 10 17 15">
            </polygon>
          </svg>
        </span>
      </div>

      <div class="mdc-select__menu mdc-menu mdc-menu-surface mdc-menu-surface--fullwidth">
        <ul class="mdc-list" role="listbox" aria-label="Food picker listbox">
          <li class="mdc-list-item mdc-list-item--selected" aria-selected="true" data-value="" role="option">
            <span class="mdc-list-item__ripple"></span>
          </li>
  `;

  for (let option of options) {
    menuHTML += `
          <li class="mdc-list-item" aria-selected="false" data-value="${option}" role="option">
            <span class="mdc-list-item__ripple"></span>
            <span class="mdc-list-item__text">${option}</span>
          </li>
  `;
  }

  menuHTML += `
      </ul>
    </div>
  </div>`;

  return menuHTML;
}