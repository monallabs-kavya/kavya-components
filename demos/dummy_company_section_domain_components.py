import kavya as kv
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import (conc_twtags,
                               tstr,
                               pd,
                               grow,
                               bg,
                               green,
                               W,
                               fc,
                               gray,
                               space,
                               y,
                               mr,
                               st,
                               srs,
                               ta)

from kavya.dsl import macros, MuCtx


def info_cards():
    with MuCtx:
        with Div(key="techonology_solutions", classes='flex items-start gap-4') as tech_solutions_box:
            with Span(classes="shrink-0 rounded-lg bg-gray-800 p-4"):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Technology Solutions:"):
                    pass

                with P(classes='mt-1 text-sm text-gray-300', text="A leader in cutting-edge technology solutions, providing innovative software and hardware solutions for businesses of all sizes. Our team of experts specializes in developing custom software, implementing scalable infrastructure, and leveraging emerging technologies to drive digital transformation"):
                    pass

    with MuCtx:            
        with Div(key="financial_services", classes='flex items-start gap-4') as financial_services_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass
            with Div():
                with H2(classes='text-lg font-bold', text="Financial Services:"):
                    pass
                with P(classes='mt-1 text-sm text-gray-300', text="At the forefront of financial services, we offer a comprehensive suite of solutions designed to empower individuals and businesses to navigate the complexities of the modern financial world with confidence and clarity. From wealth management and investment advisory to retirement planning and estate management, our seasoned team of financial advisors provides personalized guidance and strategic insights to help clients achieve their financial goals and secure their financial future. With a steadfast commitment to integrity, transparency, and fiduciary responsibility, we strive to build lasting relationships founded on trust, professionalism, and unwavering dedication to our clients' success."):

                    pass

    with MuCtx:                            
        with Div(key="healthcare_innovations", classes='flex items-start gap-4') as healthcare_innovations_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Healthcare Innovations:"):
                    pass

                with P(classes='mt-1 text-sm text-gray-300', text="Driven by a relentless pursuit of excellence, we are dedicated to revolutionizing healthcare through groundbreaking innovations and transformative technologies that improve patient outcomes, enhance clinical workflows, and advance medical science. Through collaborative partnerships with leading healthcare providers, research institutions, and technology innovators, we leverage cutting-edge developments in areas such as precision medicine, digital health, and telemedicine to address the most pressing challenges facing healthcare today. From novel treatments and therapies to state-of-the-art medical devices and diagnostic tools, our innovative solutions are reshaping the future of healthcare delivery, driving improvements in quality, accessibility, and affordability for patients and providers alike."):
                    pass


    with MuCtx:
        with Div(key="green_energy", classes='flex items-start gap-4') as green_energy_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Green Energy Solutions:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="As champions of sustainability and environmental stewardship, we are leading the charge in the transition to a cleaner, greener energy future through our innovative green energy solutions. From renewable energy projects and energy-efficient technologies to carbon reduction strategies and sustainability initiatives, we are committed to driving positive change and mitigating the impacts of climate change on our planet. By harnessing the power of renewable resources such as solar, wind, and hydroelectric energy, we are pioneering innovative solutions that promote energy independence, reduce greenhouse gas emissions, and create a more sustainable future for generations to come."):
                    pass


    with MuCtx:
        with Div(key="retail_consumer", classes='flex items-start gap-4') as retail_consumer_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Retail and Consumer Goods:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="At the forefront of retail and consumer goods, we are committed to delivering exceptional value, quality, and convenience to consumers worldwide. From fashion and apparel to electronics and home goods, our extensive portfolio of products and services caters to the diverse needs and preferences of today's discerning shoppers. Through our omnichannel retail platform and e-commerce ecosystem, we offer seamless shopping experiences that blend the best of online and offline retail, providing customers with access to a wide range of products, personalized recommendations, and convenient delivery options. With a focus on innovation, sustainability, and customer satisfaction, we are dedicated to shaping the future of retail and redefining the way consumers shop, discover, and engage with brands."):
                    pass

                
    with MuCtx:
        with Div(key = "transport_and_logistics", classes='flex items-start gap-4') as transport_and_logistics_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Transportation and Logistics:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="As leaders in transportation and logistics, we are committed to delivering efficient, reliable, and sustainable supply chain solutions that keep goods moving seamlessly across the globe. From freight forwarding and logistics management to warehousing and distribution, our comprehensive suite of services is designed to optimize the flow of goods, reduce transit times, and minimize costs for businesses of all sizes. Through our extensive network of carriers, partners, and facilities, we provide end-to-end visibility and control over the entire supply chain, enabling our customers to streamline operations, mitigate risks, and maximize efficiency in today's rapidly evolving global marketplace."):
                    pass


    with MuCtx:
        with Div(key="real_estate", classes='flex items-start gap-4') as real_estate_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Real Estate Development:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="At the forefront of real estate development, we specialize in creating vibrant, sustainable communities that enrich the lives of residents and businesses alike. From residential developments and commercial properties to mixed-use projects and industrial parks, our diverse portfolio showcases our commitment to excellence in design, construction, and placemaking. By integrating smart technologies, sustainable practices, and innovative design principles into our projects, we create environments that foster connectivity, creativity, and community engagement. With a focus on quality, integrity, and long-term value creation, we are dedicated to shaping the future of real estate and enhancing the quality of life for generations to come."):
                    pass


    with MuCtx:
        with Div(key="digital_marketing", classes='flex items-start gap-4') as digital_marketing_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Digital Marketing:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="As leaders in digital marketing, we specialize in crafting comprehensive, data-driven strategies that drive results and deliver measurable ROI for our clients. From search engine optimization (SEO) and social media marketing to content creation and email campaigns, our team of digital marketing experts leverages the latest tools and techniques to help businesses succeed in today's competitive online landscape. By understanding our clients' unique goals, target audiences, and competitive landscape, we develop customized marketing strategies that maximize reach, engagement, and conversions across digital channels. With a focus on innovation, creativity, and ROI-driven results, we empower businesses to thrive and succeed in the digital age."):
                    pass

    with MuCtx:
        with Div(key="education_training", classes='flex items-start gap-4') as education_training_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Education and Training:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="Dedicated to empowering individuals and organizations to achieve their full potential, we offer high-quality educational programs and training services designed to inspire lifelong learning and personal growth. From academic courses and professional certifications to leadership development and executive training, our comprehensive curriculum covers a wide range of topics and disciplines to meet the diverse needs and interests of our students. With a focus on experiential learning, practical skills development, and real-world applications, we equip learners with the knowledge, skills, and confidence they need to succeed in their careers and make a positive impact in their communities."):
                    pass

    with MuCtx:
        with Div(key="entertainment_and_media", classes='flex items-start gap-4') as entertainment_and_media_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Entertainment and Media:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="As creators of captivating entertainment experiences, we are committed to shaping culture, inspiring audiences, and bringing stories to life through the power of film, television, and digital media. From blockbuster movies and award-winning TV series to immersive gaming experiences and interactive content, our diverse portfolio showcases our passion for storytelling and our dedication to delivering engaging, entertaining, and thought-provoking experiences that resonate with audiences worldwide. With a focus on creativity, innovation, and storytelling excellence, we are dedicated to pushing the boundaries of entertainment and media and creating memorable experiences that entertain, enlighten, and inspire audiences of all ages."):
                    pass


    with MuCtx:
        with Div(key="food_and_beverage", classes='flex items-start gap-4') as food_and_beverage_box:
            with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                with FontAwesomeIcon(label="faGraduationCap",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="solid",
                                         mdi_label="cap",
                                         classes="w-5 h-5",
                            
                                 ):
                    pass

            with Div():
                with H2(classes='text-lg font-bold', text="Food and Beverage:"):
                    pass


                with P(classes='mt-1 text-sm text-gray-300', text="At the forefront of culinary excellence, we offer a diverse range of delicious food and beverage products that tantalize the taste buds and satisfy the cravings of food enthusiasts everywhere. From gourmet cuisine and artisanal delicacies to refreshing beverages and indulgent treats, our extensive portfolio showcases our commitment to quality, taste, and culinary innovation. By sourcing the finest ingredients, embracing culinary diversity, and leveraging the latest culinary trends, we create unforgettable dining experiences that delight the senses and nourish the soul. With a focus on sustainability, authenticity, and culinary excellence, we are dedicated to pushing the boundaries of flavor and redefining the art of dining for food lovers everywhere."):
                    pass
                            
                            
    return [tech_solutions_box, financial_services_box, healthcare_innovations_box, green_energy_box, retail_consumer_box,
                      transport_and_logistics_box, real_estate_box, education_training_box, entertainment_and_media_box,
                      food_and_beverage_box]




def GridUSP():
    
    with MuCtx:
        with HM.Div(classes='bg-gray-900 text-white') as comp_box:

            with HM.Div(classes='max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16'):
                with Div(classes='max-w-xl'):
                    with H2(classes='text-3xl font-bold sm:text-4xl', text="What makes us special"):
                        pass
                        

                    with P(classes='mt-4 text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat dolores iure fugit totam iste obcaecati. Consequatur ipsa quod ipsum sequi culpa delectus, cumque id tenetur quibusdam, quos fuga minima."):
                        pass

                with HM.Div(classes='mt-4 flex flex-wrap gap-3') as undock_btns_bar:
                    pass

                
                with HM.Div(classes='mt-8 grid grid-cols-1 gap-8 md:mt-16 md:grid-cols-2 md:gap-12 lg:grid-cols-3') as info_box_container:
                    pass
                            
    return comp_box, undock_btns_bar,  info_box_container



# # a bar to place docked components
# def undock_btns_bar():
#     with writer_ctx:
#         with HCCMutable_Div(classes='flex flex-wrap gap-3') as comp_box:
#             with Legend(classes='sr-only', text='Color'):
#                 pass
#             pass

#     return comp_box

