/**
 * Recipe Finder - Frontend JavaScript
 * Handles: dark mode, mobile nav, ingredient tags, favorites, pantry, meal planner
 */

// ============================================================
// DARK MODE
// ============================================================
(function initTheme() {
    const savedTheme = localStorage.getItem('recipeFinderTheme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme = savedTheme || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeIcon(theme);
})();

function updateThemeIcon(theme) {
    const icon = document.querySelector('.theme-icon');
    if (icon) {
        icon.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
}

const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
    themeToggle.addEventListener('click', function () {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('recipeFinderTheme', next);
        updateThemeIcon(next);
    });
}

// ============================================================
// MOBILE NAVIGATION
// ============================================================
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
if (navToggle && navMenu) {
    navToggle.addEventListener('click', function () {
        navMenu.classList.toggle('active');
    });
    // Close menu when clicking a link
    navMenu.querySelectorAll('.nav-link').forEach(function (link) {
        link.addEventListener('click', function () {
            navMenu.classList.remove('active');
        });
    });
}

// ============================================================
// INGREDIENT TAG INPUT SYSTEM
// ============================================================
function createTagInput(config) {
    const tagsContainer = document.getElementById(config.tagsId);
    const input = document.getElementById(config.inputId);
    const hiddenInput = document.getElementById(config.hiddenInputId);
    if (!tagsContainer || !input || !hiddenInput) return;

    let tags = [];

    function render() {
        tagsContainer.innerHTML = '';
        tags.forEach(function (tag, index) {
            const tagEl = document.createElement('span');
            tagEl.className = 'ingredient-tag';
            tagEl.innerHTML = escapeHtml(tag) + '<button type="button" class="ingredient-tag-remove" data-index="' + index + '">&times;</button>';
            tagsContainer.appendChild(tagEl);
        });
        hiddenInput.value = tags.join(',');
    }

    function addTag(value) {
        const clean = value.trim().toLowerCase();
        if (clean && tags.indexOf(clean) === -1) {
            tags.push(clean);
            render();
        }
        input.value = '';
    }

    function removeTag(index) {
        tags.splice(index, 1);
        render();
    }

    input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ',') {
            e.preventDefault();
            addTag(input.value);
        } else if (e.key === 'Backspace' && input.value === '' && tags.length > 0) {
            removeTag(tags.length - 1);
        }
    });

    input.addEventListener('blur', function () {
        if (input.value.trim()) {
            addTag(input.value);
        }
    });

    tagsContainer.addEventListener('click', function (e) {
        if (e.target.classList.contains('ingredient-tag-remove')) {
            removeTag(parseInt(e.target.getAttribute('data-index'), 10));
        }
    });

    // Quick add buttons
    document.querySelectorAll('.quick-tag[data-ingredient]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            addTag(btn.getAttribute('data-ingredient'));
            input.focus();
        });
    });

    render();
}

createTagInput({ tagsId: 'heroTags', inputId: 'heroInput', hiddenInputId: 'heroHiddenInput' });
createTagInput({ tagsId: 'findTags', inputId: 'findInput', hiddenInputId: 'findHiddenInput' });

// ============================================================
// FAVORITES (Local Storage) - Single shared system
// ============================================================
var FAVORITES_KEY = 'recipeFinderFavorites';

function getFavorites() {
    try {
        var data = localStorage.getItem(FAVORITES_KEY);
        if (!data) return [];
        var parsed = JSON.parse(data);
        if (!Array.isArray(parsed)) return [];
        // Normalize all IDs to integers
        return parsed.map(function (id) { return parseInt(id, 10); })
                      .filter(function (id) { return !isNaN(id); });
    } catch (e) {
        return [];
    }
}

function saveFavorites(favs) {
    localStorage.setItem(FAVORITES_KEY, JSON.stringify(favs));
}

function isFavorite(id) {
    var numId = parseInt(id, 10);
    return getFavorites().indexOf(numId) !== -1;
}

function addFavorite(id) {
    var numId = parseInt(id, 10);
    var favs = getFavorites();
    if (favs.indexOf(numId) === -1) {
        favs.push(numId);
        saveFavorites(favs);
    }
    updateFavoriteButtons();
}

function removeFavorite(id) {
    var numId = parseInt(id, 10);
    var favs = getFavorites();
    var index = favs.indexOf(numId);
    if (index !== -1) {
        favs.splice(index, 1);
        saveFavorites(favs);
    }
    updateFavoriteButtons();
}

function toggleFavorite(id) {
    var numId = parseInt(id, 10);
    if (isFavorite(numId)) {
        removeFavorite(numId);
    } else {
        addFavorite(numId);
    }
}

function updateFavoriteButtons() {
    var favs = getFavorites();
    var buttons = document.querySelectorAll('.favorite-btn');
    buttons.forEach(function (btn) {
        var id = parseInt(btn.getAttribute('data-recipe-id'), 10);
        var heart = btn.querySelector('.heart');
        if (favs.indexOf(id) !== -1) {
            btn.classList.add('active');
            if (heart) heart.textContent = '♥';
        } else {
            btn.classList.remove('active');
            if (heart) heart.textContent = '♡';
        }
    });
}

// Global click handler for all favorite buttons
document.addEventListener('click', function (e) {
    var btn = e.target.closest('.favorite-btn');
    if (btn) {
        e.preventDefault();
        e.stopPropagation();
        var id = parseInt(btn.getAttribute('data-recipe-id'), 10);
        toggleFavorite(id);
        // If on favorites page, remove the card if unfavorited
        if (window.location.pathname === '/favorites') {
            var card = btn.closest('.recipe-card');
            if (card && !isFavorite(id)) {
                card.remove();
                // Check if no favorites left
                var remaining = document.querySelectorAll('#favoritesGrid .recipe-card');
                if (remaining.length === 0) {
                    var noFavs = document.getElementById('noFavorites');
                    var grid = document.getElementById('favoritesGrid');
                    if (noFavs) noFavs.style.display = 'block';
                    if (grid) grid.style.display = 'none';
                }
            }
        }
    }
});

updateFavoriteButtons();

// Cross-tab synchronization
window.addEventListener('storage', function (e) {
    if (e.key === FAVORITES_KEY) {
        updateFavoriteButtons();
        if (window.location.pathname === '/favorites') {
            loadFavoritesPage();
        }
    }
});

// ============================================================
// FAVORITES PAGE - Load and display favorited recipes
// ============================================================
function loadFavoritesPage() {
    var grid = document.getElementById('favoritesGrid');
    var noFavs = document.getElementById('noFavorites');
    if (!grid) return;

    var favs = getFavorites();
    if (favs.length === 0) {
        noFavs.style.display = 'block';
        grid.style.display = 'none';
        return;
    }

    noFavs.style.display = 'none';
    grid.style.display = 'grid';
    grid.innerHTML = '';

    // Fetch recipe data from the server
    fetch('/api/recipes')
        .then(function (r) { return r.json(); })
        .then(function (data) {
            var recipes = data.recipes || data;
            var favRecipes = recipes.filter(function (r) {
                return favs.indexOf(parseInt(r.id, 10)) !== -1;
            });
            favRecipes.forEach(function (recipe) {
                grid.appendChild(createRecipeCard(recipe));
            });
            updateFavoriteButtons();
        })
        .catch(function () {
            noFavs.querySelector('p').textContent = 'Unable to load favorites. Please try again.';
            noFavs.style.display = 'block';
        });
}

function createRecipeCard(recipe) {
    const card = document.createElement('div');
    card.className = 'recipe-card';
    var fallbackImg = 'https://images.unsplash.com/photo-1495521821757-a1efb6729352?w=800&q=80';
    card.innerHTML =
        '<div class="recipe-card-image">' +
            '<img src="' + recipe.image + '" alt="' + escapeHtml(recipe.name) + '" loading="lazy" onerror="this.onerror=null;this.src=\'' + fallbackImg + '\'">' +
            '<button class="favorite-btn" data-recipe-id="' + recipe.id + '" aria-label="Add to favorites"><span class="heart">♡</span></button>' +
            '<span class="recipe-badge">' + escapeHtml(recipe.category) + '</span>' +
        '</div>' +
        '<div class="recipe-card-body">' +
            '<h3 class="recipe-card-title">' + escapeHtml(recipe.name) + '</h3>' +
            '<p class="recipe-card-desc">' + escapeHtml(recipe.description.substring(0, 80)) + '...</p>' +
            '<div class="recipe-card-meta">' +
                '<span class="meta-item">⏱️ ' + recipe.total_time + ' min</span>' +
                '<span class="meta-item">📊 ' + escapeHtml(recipe.difficulty) + '</span>' +
            '</div>' +
            '<a href="/recipe/' + recipe.id + '" class="btn btn-primary btn-sm btn-block">View Recipe</a>' +
        '</div>';
    return card;
}

loadFavoritesPage();

// ============================================================
// PANTRY (Local Storage)
// ============================================================
function getPantry() {
    try {
        const data = localStorage.getItem('recipeFinderPantry');
        return data ? JSON.parse(data) : [];
    } catch (e) {
        return [];
    }
}

function savePantry(items) {
    localStorage.setItem('recipeFinderPantry', JSON.stringify(items));
}

function renderPantry() {
    const container = document.getElementById('pantryTags');
    const countEl = document.getElementById('pantryCount');
    const searchInput = document.getElementById('pantrySearchInput');
    if (!container) return;

    const items = getPantry();
    countEl.textContent = items.length + ' item' + (items.length !== 1 ? 's' : '');
    searchInput.value = items.join(',');

    if (items.length === 0) {
        container.innerHTML = '<p class="pantry-empty">Your pantry is empty. Add some ingredients!</p>';
        return;
    }

    container.innerHTML = '';
    items.forEach(function (item, index) {
        const tag = document.createElement('span');
        tag.className = 'ingredient-tag';
        tag.innerHTML = escapeHtml(item) + '<button type="button" class="ingredient-tag-remove" data-index="' + index + '">&times;</button>';
        container.appendChild(tag);
    });
}

const pantryForm = document.getElementById('pantryForm');
if (pantryForm) {
    pantryForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const input = document.getElementById('pantryInput');
        const value = input.value.trim().toLowerCase();
        if (value) {
            const items = getPantry();
            if (items.indexOf(value) === -1) {
                items.push(value);
                savePantry(items);
                renderPantry();
            }
            input.value = '';
        }
    });
}

const pantryTags = document.getElementById('pantryTags');
if (pantryTags) {
    pantryTags.addEventListener('click', function (e) {
        if (e.target.classList.contains('ingredient-tag-remove')) {
            const items = getPantry();
            items.splice(parseInt(e.target.getAttribute('data-index'), 10), 1);
            savePantry(items);
            renderPantry();
        }
    });
}

const clearPantryBtn = document.getElementById('clearPantry');
if (clearPantryBtn) {
    clearPantryBtn.addEventListener('click', function () {
        if (confirm('Clear all pantry items?')) {
            savePantry([]);
            renderPantry();
        }
    });
}

renderPantry();

// ============================================================
// MEAL PLANNER (Local Storage)
// ============================================================
function getMealPlan() {
    try {
        const data = localStorage.getItem('recipeFinderMealPlan');
        return data ? JSON.parse(data) : {};
    } catch (e) {
        return {};
    }
}

function saveMealPlan(plan) {
    localStorage.setItem('recipeFinderMealPlan', JSON.stringify(plan));
}

function renderMealPlan() {
    const plan = getMealPlan();
    document.querySelectorAll('.planner-slot').forEach(function (slot) {
        const day = slot.getAttribute('data-day');
        const meal = slot.getAttribute('data-meal');
        const key = day + '-' + meal;
        const content = slot.querySelector('.slot-content');

        if (plan[key]) {
            content.innerHTML = '<span class="slot-recipe">' + escapeHtml(plan[key].name) + '</span>';
            content.title = 'Click to change';
        } else {
            content.innerHTML = '<span class="slot-empty">+ Add</span>';
        }
    });
}

document.addEventListener('click', function (e) {
    const slot = e.target.closest('.planner-slot');
    if (slot) {
        openRecipePicker(slot);
    }
});

let currentSlot = null;

function openRecipePicker(slot) {
    currentSlot = slot;
    const modal = document.getElementById('recipePickerModal');
    const searchInput = document.getElementById('modalSearch');
    const recipesContainer = document.getElementById('modalRecipes');

    modal.classList.add('active');
    searchInput.value = '';
    recipesContainer.innerHTML = '<p style="text-align:center;padding:20px;color:var(--color-text-muted);">Loading recipes...</p>';

    fetch('/api/recipes')
        .then(function (r) { return r.json(); })
        .then(function (data) {
            var recipes = data.recipes || data;
            renderModalRecipes(recipes, '');
            searchInput.addEventListener('input', function () {
                renderModalRecipes(recipes, searchInput.value);
            });
        })
        .catch(function () {
            recipesContainer.innerHTML = '<p style="text-align:center;padding:20px;color:var(--color-text-muted);">Unable to load recipes.</p>';
        });
}

function renderModalRecipes(recipes, filter) {
    const container = document.getElementById('modalRecipes');
    const query = filter.toLowerCase();
    const filtered = recipes.filter(function (r) {
        return r.name.toLowerCase().indexOf(query) !== -1 ||
               r.category.toLowerCase().indexOf(query) !== -1;
    });

    if (filtered.length === 0) {
        container.innerHTML = '<p style="text-align:center;padding:20px;color:var(--color-text-muted);">No recipes found.</p>';
        return;
    }

    container.innerHTML = '';
    filtered.forEach(function (recipe) {
        const item = document.createElement('div');
        item.className = 'modal-recipe-item';
        item.innerHTML =
            '<img src="' + recipe.image + '" alt="' + escapeHtml(recipe.name) + '">' +
            '<div class="modal-recipe-item-info">' +
                '<div class="modal-recipe-item-name">' + escapeHtml(recipe.name) + '</div>' +
                '<div class="modal-recipe-item-meta">' + escapeHtml(recipe.category) + ' · ' + recipe.total_time + ' min</div>' +
            '</div>';
        item.addEventListener('click', function () {
            selectRecipeForSlot(recipe);
        });
        container.appendChild(item);
    });
}

function selectRecipeForSlot(recipe) {
    if (!currentSlot) return;
    const day = currentSlot.getAttribute('data-day');
    const meal = currentSlot.getAttribute('data-meal');
    const key = day + '-' + meal;

    const plan = getMealPlan();
    plan[key] = { id: recipe.id, name: recipe.name };
    saveMealPlan(plan);
    renderMealPlan();

    closeModal();
}

function closeModal() {
    const modal = document.getElementById('recipePickerModal');
    if (modal) modal.classList.remove('active');
    currentSlot = null;
}

const modalClose = document.getElementById('modalClose');
if (modalClose) modalClose.addEventListener('click', closeModal);

const modalOverlay = document.querySelector('.modal-overlay');
if (modalOverlay) modalOverlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
});

const clearPlannerBtn = document.getElementById('clearPlanner');
if (clearPlannerBtn) {
    clearPlannerBtn.addEventListener('click', function () {
        if (confirm('Clear the entire meal plan?')) {
            saveMealPlan({});
            renderMealPlan();
        }
    });
}

renderMealPlan();

// ============================================================
// UTILITY FUNCTIONS
// ============================================================
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ============================================================
// SMOOTH SCROLL FOR ANCHOR LINKS
// ============================================================
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// ============================================================
// NAVBAR SCROLL EFFECT
// ============================================================
let lastScroll = 0;
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    const currentScroll = window.pageYOffset;
    if (currentScroll > 10) {
        navbar.style.boxShadow = '0 2px 12px var(--color-shadow)';
    } else {
        navbar.style.boxShadow = 'none';
    }
    lastScroll = currentScroll;
}, { passive: true });
