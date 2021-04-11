from classes import food

Food = food.Food

def gen_foods(context):
    foods = [        
        Food(0, 'Amaranth', 6, 6, 9, 9, 6, context.files.imgs.amaranth,
            [
                "Climate+Temperature: Consistent warmth and sunlight",
                "Labour Inputs: Approx. 5 minutes a day for weeding\nand misting",
                "Fertilizer: Adapts to most soils, but grows best in\nfertile, well-drained loam"
            ],
            "1-3 months; 1 month for leaves and 3 months for seeds",
            [
                "Type of Crop:  Gluten-free grain",
                "Minerals + Nutrients: Fibre, protein, antioxidants,\nmicronutrients, vitamin C, magnesium, potassium,\nphosphorous, iron and vitamin E;\nleaves contain vitamin A, C and folate"
            ],
            [
                "Minimum of 300cm^2 needed to harvest",
                "Tiny box to store several seeds, Amaranth plant can\nbe composted to create fertilizer",
                "Amaranth seeds can be kept for up to 3 years",
                "Amaranth can reseed itself for several years\n(only initial planting required)",
            ],
            [
                "Reduces inflammation and lowers cholesterol"
            ]
        ),
        Food (1, 'Ginger', 5, 3, 8, 4, 6, context.files.imgs.ginger,
            [
                "Climate+Temperature: Full shade, relatively\ncolder temperature",
                "Labour Inputs:  2 minutes a day to water",
                "Fertilizer: rich, loose soil\n(add compost and/or manure)",
            ],
            "8-10 months to have a fully grown ginger plant",
            [
                "Vitamin C and B6, iron, potassium, magnesium,\nand other minerals and micronutrients"
            ],
            [
                "A minimum of 100cm2 needed to harvest",
                "Can be preserved in small boxes, refrigerated\nfor up to a month; can be dried but does not provide much nutritional value when dried",
                "Produces a large harvest"
            ],
            [
                "Reduces muscle pain and soreness, nausea and\nmorning sickness, inflammation, aids in digestion, lowers cholesterol levels, reduces the risk of infections, strengthens the immune system"
            ]
        ),

        Food(2, 'Asparagus', 10, 10, 10, 10, 10, context.files.imgs.asparagus,
            ["To Be Updated"], "To Be Updated", ["To Be Updated"], ["To Be Updated"], ["To Be Updated"]
        ),
        
        Food(3, 'Barley', 10, 10, 10, 10, 10, context.files.imgs.barley,
            ["To Be Updated"], "To Be Updated", ["To Be Updated"], ["To Be Updated"], ["To Be Updated"]
        ),
        
        Food(4, 'Basil', 10, 10, 10, 10, 10, context.files.imgs.basil,
            ["To Be Updated"], "To Be Updated", ["To Be Updated"], ["To Be Updated"], ["To Be Updated"]
        ),
        
        Food(5, 'Beetroot', 10, 10, 10, 10, 10, context.files.imgs.beetroot,
            ["To Be Updated"], "To Be Updated", ["To Be Updated"], ["To Be Updated"], ["To Be Updated"]
        ),

        Food(6, 'Strawberry', 7, 7, 6, 5, 6, context.files.imgs.strawberry,
            [
                "Climate+Temperature: direct sunlight for\n6 - 10 hours a day, 60 - 80 degrees Fahrenheit (ideal temp)",
                "Labour Inputs: water daily for best results\n(keep soil moist), weed daily (by hand)",
                "Fertilizer: Are tolerant of most soils, but\ngrows best in fertile, well-drained loam"
            ],
            "Ready to harvest 4-6 weeks after flowers bloom (Approximately 3 months)",
            [
                "Vitamin C and manganese, vitamin B9, antioxidants"
            ],
            [
                "Store in closed and refrigerated container",
                "Lasts up to 2 weeks most",
                "Can be dried but does not provide many nutritional benefits",
                "Plant lasts up to 6 years (reproduces naturally\nonce a year based on cycle)"
            ],
            [
                "Controls blood sugar, good heart health, can help\nprevent cardiovascular disease and other\ndiseases, guards against cancer and increases\nHDL (good) cholesterol"
            ]
        ),
        Food(7, 'Spinach', 8, 8, 8, 7, 6, context.files.imgs.spinach,
            [
                "Climate: Cool weather (spring/fall temperatures)",
                "Labour Inputs : 3-4 light waterings a week",
                "Fertilizer: moist, nitrogen-rich soil"
            ],
            "Approx. 6 weeks",
            [
                "High in calcium, magnesium and iron, reduces\nblood sugar, improves eyesight, helps bone\ngrowth and maintenance, reduces cholesterol",
                "Also contains folate, vitamins B6, B9, C, and K, iron, carotenoids, potassium"
            ],
            [
                "Wash, package and refrigerate spinach",
                "Can be preserved up to 3 weeks, frozen can be\npreserved for up to 8 weeks but loses\nnutritional value in the process",
                "Regenerates for up to 4 harvests, but can expand to create new plants; reseeds on its own"
            ],
            [
                "Reduces blood sugar, improves eyesight, helps\nbone growth and maintenance, reduces cholesterol"
            ]
        ),
        Food(8, 'Potatoes', 6, 6, 7, 8, 7, context.files.imgs.potatoes,
            [
                "Climate+Temperature: temperate conditions,\nfull sun",
                "Labour Inputs: Water every other day and\nsoil maintenance every week",
                "Fertilizer: light, loose, well-drained soil,\nphosphate and potassium is beneficial"
            ],
            "Approx. 10 weeks after potato flowers",
            [
                "Rich in fiber, antioxidants, magnesium, vitamins\nB6 and C, copper, manganese, niacin,\nand phosphorus."
            ],
            [
                "Store in a cool dark area",
                "Keep open (do not seal unless its roots)",
                "Can store open potatoes for up to 2 months,\n5 months if frozen",
                "Easy to grow more harvest from existing harvest"
            ],
            [
                "Improved blood sugar control, reduced heart\ndisease risk and higher immunity, filling for long periods of time"
            ]
        ),
        Food(9, 'Wheat', 4, 4, 7, 9, 7, context.files.imgs.wheat,
            [
                "Climate: In and out of the sun",
                "Temperature: Requires cold and hot\ntemperatures",
                "Labour Inputs: 4-5 hours",
                "Fertilizer: Phosphorous start soil"
            ],
            "Approximately 8 months (3 seasons)",
            [
                "Niacin, fibre, vitamin B6, manganese, selenium,\niron, copper, folate and niacin,\namong other minerals"
            ],
            [
                "Minimum of 10m^2 needed to harvest",
                "Packaged and can be stored up to 3 years",
                "Must be harvested each year/ season but\nharvests are large and last long"
            ],
            [
                "Supports digestion, reduce risks of obesity,\nlowers risks of stroke and heart disease and prevents of celiac disease"
            ]
        )
    ]
    return foods

