// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="chapter_0.html"><strong aria-hidden="true">1.</strong> 介绍</a></li><li class="chapter-item expanded affix "><li class="part-title">正文</li><li class="chapter-item expanded "><a href="chapter_1.html"><strong aria-hidden="true">2.</strong> 第 1 章 向量</a></li><li class="chapter-item expanded "><a href="chapter_2.html"><strong aria-hidden="true">3.</strong> 第 2 章矩阵</a></li><li class="chapter-item expanded "><a href="chapter_3.html"><strong aria-hidden="true">4.</strong> 第 3 章线性方程组</a></li><li class="chapter-item expanded "><a href="chapter_4.html"><strong aria-hidden="true">5.</strong> 第 4 章 向量空间</a></li><li class="chapter-item expanded "><a href="chapter_5.html"><strong aria-hidden="true">6.</strong> 第 5 章线性变换</a></li><li class="chapter-item expanded "><a href="chapter_6.html"><strong aria-hidden="true">7.</strong> 第 6 章行列式</a></li><li class="chapter-item expanded "><a href="chapter_7.html"><strong aria-hidden="true">8.</strong> 第 7 章内积空间</a></li><li class="chapter-item expanded "><a href="chapter_8.html"><strong aria-hidden="true">9.</strong> 第 8 章 特征值和特征向量</a></li><li class="chapter-item expanded "><a href="chapter_9.html"><strong aria-hidden="true">10.</strong> 第 9 章 二次型和谱定理</a></li><li class="chapter-item expanded "><a href="chapter_10.html"><strong aria-hidden="true">11.</strong> 第 10 章 线性代数实践</a></li><li class="chapter-item expanded affix "><li class="part-title">笔记</li><li class="chapter-item expanded "><a href="chapter_11.html"><strong aria-hidden="true">12.</strong> 第 1 章 笔记</a></li><li class="chapter-item expanded "><a href="chapter_14.html"><strong aria-hidden="true">13.</strong> 第 4 章 笔记</a></li><li class="chapter-item expanded "><a href="chapter_15.html"><strong aria-hidden="true">14.</strong> 第 5 章 笔记</a></li><li class="chapter-item expanded "><a href="chapter_16.html"><strong aria-hidden="true">15.</strong> 第 6 章 笔记</a></li><li class="chapter-item expanded "><a href="chapter_17.html"><strong aria-hidden="true">16.</strong> 第 7 章 笔记</a></li><li class="chapter-item expanded "><a href="chapter_18.html"><strong aria-hidden="true">17.</strong> 第 8 章 笔记</a></li><li class="chapter-item expanded affix "><li class="part-title">附录</li><li class="chapter-item expanded "><a href="chapter_100_ml-key-math-eqns.html"><strong aria-hidden="true">18.</strong> The Most Important Machine Learning Equations: A Comprehensive Guide</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0].split("?")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
