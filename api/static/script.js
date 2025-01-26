document.addEventListener("DOMContentLoaded", () => {
    const highlights = document.querySelectorAll(".hovertext");
    
    // Store original background colors in a map
    const originalColors = new Map();
    
    highlights.forEach((element) => {
        // Extract the original background color from the style attribute
        const style = element.getAttribute('style');
        const bgColor = style.match(/background-color: ([^;]+)/)[1];
        
        // Store the original color using the highlight class as key
        const highlightClass = Array.from(element.classList)
            .find(cls => cls.startsWith('similarity-'));
        if (highlightClass) {
            originalColors.set(highlightClass, bgColor);
        }
        
        element.addEventListener("mouseenter", () => {
            const highlightClass = Array.from(element.classList)
                .find(cls => cls.startsWith('similarity-'));
            
            if (highlightClass) {
                const hoverStyle = element.getAttribute('data-hover-style');
                const hoverColor = hoverStyle.match(/background-color: ([^;]+)/)[1];
                
                document.querySelectorAll(`.${highlightClass}`).forEach((el) => {
                    el.style.backgroundColor = hoverColor;
                });
            }
        });

        element.addEventListener("mouseleave", () => {
            const highlightClass = Array.from(element.classList)
                .find(cls => cls.startsWith('similarity-'));
            
            if (highlightClass) {
                const originalColor = originalColors.get(highlightClass);
                document.querySelectorAll(`.${highlightClass}`).forEach((el) => {
                    el.style.backgroundColor = originalColor;
                });
            }
        });
    });
});
