---
name: Technical Precision Portfolio
colors:
  surface: '#121416'
  surface-dim: '#121416'
  surface-bright: '#38393c'
  surface-container-lowest: '#0c0e10'
  surface-container-low: '#1a1c1e'
  surface-container: '#1e2022'
  surface-container-high: '#282a2c'
  surface-container-highest: '#333537'
  on-surface: '#e2e2e5'
  on-surface-variant: '#bccbb6'
  inverse-surface: '#e2e2e5'
  inverse-on-surface: '#2f3133'
  outline: '#869582'
  outline-variant: '#3d4a3b'
  surface-tint: '#4be260'
  primary: '#5bf06c'
  on-primary: '#00390c'
  primary-container: '#39d353'
  on-primary-container: '#005517'
  inverse-primary: '#006e20'
  secondary: '#a2c9ff'
  on-secondary: '#00315b'
  secondary-container: '#3994ef'
  on-secondary-container: '#002b50'
  tertiary: '#ffc7c0'
  on-tertiary: '#591b17'
  tertiary-container: '#ff9f94'
  on-tertiary-container: '#79332d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6fff7b'
  primary-fixed-dim: '#4be260'
  on-primary-fixed: '#002205'
  on-primary-fixed-variant: '#005316'
  secondary-fixed: '#d3e4ff'
  secondary-fixed-dim: '#a2c9ff'
  on-secondary-fixed: '#001c38'
  on-secondary-fixed-variant: '#004881'
  tertiary-fixed: '#ffdad6'
  tertiary-fixed-dim: '#ffb4ab'
  on-tertiary-fixed: '#3d0605'
  on-tertiary-fixed-variant: '#76312b'
  background: '#121416'
  on-background: '#e2e2e5'
  surface-variant: '#333537'
typography:
  display:
    fontFamily: Inter
    fontSize: 56px
    fontWeight: '600'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.005em
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: -0.01em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-mono-bold:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.06em
  label-mono-muted:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit-2xs: 0.25rem
  unit-xs: 0.5rem
  unit-sm: 0.75rem
  unit-md: 1rem
  unit-lg: 1.5rem
  unit-xl: 2rem
  unit-2xl: 3rem
  unit-3xl: 4rem
  unit-4xl: 6rem
  gutter-desktop: 1.5rem
  gutter-mobile: 1rem
  container-max: 1280px
---

## Brand & Style

This design system establishes an ultra-focused, data-driven engineering aesthetic tailored for an elite AI and Data Science practitioner. The core philosophy merges the utility of high-end developer tooling with the disciplined restraint of modernist technical publications. The target audience encompasses engineering leaders, research scientists, and technical founders who evaluate systems on architecture, algorithmic rigor, and measurable outcomes.

Rather than succumbing to cyberpunk pastiche, skeuomorphic circuits, or glowing neon cliches, the system uses an austere, dark-mode terminal posture:
- **Disciplined Minimalism:** Deep charcoal voids, precise alignment grids, and strict spatial cadence communicate quiet authority.
- **Instrument-Grade Information Hierarchy:** Visual weight is governed strictly by data density, monospaced metadata arrays, and measured typographic contrast.
- **Tactile Technical Accents:** Vibrant tones are deployed exclusively to indicate operational state, test coverage, model convergence, and verified actions.

## Colors

The palette operates on calibrated low-reflectance charcoal and slate values, allowing high-signal data points to surface immediately without visual fatigue.

### System Palette
- **Canvas Base (`#08090A`):** Deep near-black background anchoring all views.
- **Surface Level 1 (`#101214`):** Base container canvas for structural panels, data tables, and major partitions.
- **Surface Level 2 (`#15181B`):** Interactive cards, code execution cells, inspector drawers, and floating panels.
- **Primary Accent (`#39D353`):** High-efficiency commit green representing production health, active model deployments, validation metrics, and primary calls to action.
- **Secondary Accent (`#4DA3FF`):** Technical cyan/cool blue used for tensor shapes, parameter dimensions, hyperparameter tags, active filters, and deep-link interactive anchors.
- **Structural Lines (`#1E2227` & `#2C3138`):** Razor-thin 1px dividers establishing structural boundaries without high-contrast distraction.

### Functional Typography Spectrum
- **Primary Text (`#F5F7F8`):** Dominant display headings, critical KPI figures, and code block statements.
- **Secondary Text (`#9AA1A8`):** Narrative summaries, documentation body copy, and secondary labels.
- **Muted Text (`#626970`):** Timestamps, column indicators, tensor index notations, and disabled triggers.

## Typography

The typographic system relies on a dual-font structure:
- **Inter:** Handles interface chrome, structured narratives, project case-study overviews, and primary titles. Geometric clarity and tight tracking give headings an engineered, architectural tone.
- **JetBrains Mono:** Handles operational readouts, algorithmic code blocks, tabular benchmarks, loss metrics, runtime specs, and tag labels.

Monospaced styles are treated as first-class citizens rather than secondary decorations, establishing parity between narrative assertions and mathematical evidence.

## Layout & Spacing

The layout is constructed on an adaptive 12-column grid governed by strict modular proportions:
- **Desktop (1024px+):** 12 columns, 24px gutters, max-width 1280px, responsive 32px-64px safe outer margins.
- **Tablet (768px - 1023px):** 8 columns, 16px gutters, 24px outer margins.
- **Mobile (320px - 767px):** 4 columns, 16px gutters, 16px outer margins. Multi-column metric dashboards collapse to stacked vertical rows with horizontal-scroll code tables.

Generous vertical macro-spacing (`unit-3xl` to `unit-4xl`) divides major portfolio domains (e.g., LLM Architecture, Model Benchmarks, Distributed Training Infrastructure), contrasting with dense, micro-spaced internal units (`unit-xs` to `unit-sm`) inside diagnostic data tables and execution cells.

## Elevation & Depth

Visual hierarchy does not rely on diffused drop shadows or floating blurs. Instead, depth is articulated through precise **tonal layering and low-contrast surface outlines**:

1. **Surface Base (`#08090A`):** The ground plane.
2. **Structural Tier (`#101214`):** Inset cards and structural sections bounded by a 1px border of `#1E2227`.
3. **Elevated Tier (`#15181B`):** Hovered cards, inspector panels, model output modals, and flyouts, framed with a 1px border of `#2C3138`.
4. **Interactive Focus:** When active or hovered, interactive panels upgrade their border to `#39D353` (25% opacity) or `#4DA3FF` (30% opacity) without drop shadows or glow halos, simulating precision CNC chamfers and LED instrumentation.

## Shapes

The design uses a restrained, semi-sharp corner radius (Soft, `roundedness: 1`):
- Standard interactive containers, cards, code previews, and inputs use `0.25rem` (4px).
- Modals, large dashboard widgets, and terminal panels use `0.5rem` (8px).
- Small tags, metadata status dots, and commit indicators remain crisp rectangles or functional circular badges.

No pill-shaped UI elements are allowed; rounded pill elements soften the technical aesthetic and reduce information density.

## Components

### 1. Buttons
- **Primary Action:** Solid `#39D353` fill, `#08090A` monospace text (`label-mono-bold`), 4px radius, 0.5rem x 1rem padding. Hover state shifts background to `#45E060`.
- **Secondary Technical:** `#15181B` background, 1px `#2C3138` border, `#F5F7F8` text. Hover upgrades border to `#4DA3FF` with text tinted `#4DA3FF`.
- **Ghost/Terminal:** Monospaced icon/label button, transparent background. Hover adds subtle `#15181B` background and `#39D353` indicator prefix (`>_`).

### 2. Chips & Status Badges
- **Status Indicator:** Flex row with a 6px circular dot (e.g., `#39D353` for live/deployed models, `#4DA3FF` for active evaluations, `#626970` for archived benchmarks), followed by uppercase `label-mono-bold` text.
- **Tech Stack Badge:** Low-profile `#101214` background, `#1E2227` outline, `#9AA1A8` monospaced text.

### 3. Cards & Architecture Nodes
- **Project/Research Card:** `#101214` background, `#1E2227` border, 4px corner radius. Padding of 1.5rem (`unit-lg`). Header displays project name in Inter `headline-sm` alongside an execution hash or repository metric in JetBrains Mono.
- **Hover Reaction:** Border shifts to `#2C3138`, and header title changes color to `#39D353`.

### 4. Input Fields & Search Bars
- **Query / Filter Field:** `#08090A` inset background, `#1E2227` border, `#F5F7F8` monospaced text. Focus state triggers a clean 1px outline of `#4DA3FF` without external shadow rings. Prompt prefix (`$`) rendered in `#626970`.

### 5. Checkboxes & Radio Controls
- **Control Box:** 14px x 14px square, 2px radius, `#101214` fill, `#2C3138` border.
- **Checked State:** Fill turns `#39D353` with a `#08090A` inner check icon.

### 6. Code Cells & Metric Readouts (Specialized)
- **Code Execution Block:** Dark slate surface (`#101214`), top bar showing language/kernel details in JetBrains Mono (`label-mono-muted`), right-aligned execution timing (`e.g., 24.2ms`). Code body formatted using standard syntax highlighting tokens rooted in electric green, technical blue, and muted grays.
- **KPI Metric Cell:** JetBrains Mono bold numerical value (`headline-lg`) paired with a micro-caption (`label-mono-muted`) pinned above the metric.