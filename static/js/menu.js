/*jshint esversion: 6 */

var menuItems = [
    {
        section: "Starters",
        items: [
            {
                title: "Buffalo Chicken Wings",
                description: "Succulent crispy chicken wings tossed in our signature buffalo sauce served with blue cheese dip.",
                price: "€8.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/buffalo-wings_xgsyjv.webp"
            },
            {
                title: "Seafood Chowder",
                description: "Chunks of freshly caught Irish seafood in a thick and creamy soup. Served with homemade sourdough bread.",
                price: "€7.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848206/seafood-chowder_zfzxgy.webp"
            },
            {
                title: "Chili Beef Nachos",
                description: "Slow cooked mexican beef on top of our homemade crunchy nachos and topped with cheese and jalepenos. Served with sour cream, salsa and guacamole.",
                price: "€9.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848206/nachos_f7ebb1.webp"
            },
            {
                title: "Mozzarella Sticks",
                description: "Deep fried sticks of mozzarella cheese served with a spicy tomato salsa",
                price: "€6.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848206/mozzarella-sticks_i0oqut.webp"
            },
        ]
    },
    {
        section: "Mains",
        items: [
            {
                title: "8oz Beef Burger",
                description: "100% Irish 8oz beef burger served on a brioche bun with bacon, cheese, tomato and our signature house sauce. Includes fries. ",
                price: "€13.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/beef-burger_uenzu3.webp"
            },
            {
                title: "Crispy Buttermilk Chicken Burger",
                description: "Buttermilk soaked crispy chicken burger served on a brioche bun with lettuce, onion, cheese, tomato and our signature house sauce. Includes fries.",
                price: "€12.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/chicken-burger_j9lloz.webp"
            },
            {
                title: "Chicken Strips and House Fries",
                description: "Buttermilk southern fried chicken strips, served with house fries and garlic mayo.",
                price: "€12.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/chicken-strips_mkycvq.webp"
            },
            {
                title: "T-Bone Steak",
                description: "T-Bone steak cooked to your liking served with house fries, onion rings and peppercorn sauce",
                price: "€18.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848206/tbone-steak_m4qzu0.webp"
            },
        ]
    },
    {
        section: "Desserts",
        items: [
            {
                title: "Peacan Pie",
                description: "A sweet treat to end your meal on a high note.",
                price: "€5.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848206/peacan-pie_jsll2u.webp"
            },
            {
                title: "Apple Pie",
                description: "An indulgent dessert to satisfy your sweet cravings.",
                price: "€5.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/apple-pie_nsjncx.webp"
            },
            {
                title: "Banana Split",
                description: "An American diner classic. Banana served with vanilla, chocolate and strawberry ice-cream, covered in chocolate sauce.",
                price: "€5.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/banana-split_y0mrnc.webp"
            },
            {
                title: "Ice Cream Sundae",
                description: "Classic ice-cream sundae. Multiple flavours available, please ask your server.",
                price: "€5.99",
                image: "https://res.cloudinary.com/dwjbpgk3s/image/upload/v1691848205/icecream-sundae_fbkhxq.webp"
            },
        ]
    }
];

function generateMenuItems() {
    var menuContainer = document.getElementById("menu-container");
    for (var i = 0; i < menuItems.length; i++) {
        var section = menuItems[i].section;
        var items = menuItems[i].items;

        var sectionHTML = `
        <div class="menu-section">
          <h2>${section}</h2>
        </div>
      `;
        menuContainer.innerHTML += sectionHTML;

        var sectionContainer = menuContainer.getElementsByClassName("menu-section")[i];
        for (var j = 0; j < items.length; j++) {
            var item = items[j];
            var itemHTML = `
          <div class="menu-item">
            <div class="menu-item-details">
              <h3 class="menu-item-title green-brand">${item.title}</h3>
              <p class="menu-item-price gold-brand">${item.price}</p>
              <p class="menu-item-description">${item.description}</p>
              <img src="${item.image}" alt="${item.title}" class="menu-item-image loading="lazy">
            </div>
          </div>
        `;
            sectionContainer.innerHTML += itemHTML;
        }
    }
}
window.onload = generateMenuItems;