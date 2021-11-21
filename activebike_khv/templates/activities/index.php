<?php
/**
 * The main template file
 *
 * This is the most generic template file in a WordPress theme
 * and one of the two required files for a theme (the other being style.css).
 * It is used to display a page when nothing more specific matches a query.
 * E.g., it puts together the home page when no home.php file exists.
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package ActiveBike_KHV
 */

get_header();
?>

	<main id="primary" class="main site-main">

    <div class="container">
        <div class="row">
                
            <div class="col-12 col-md-4">
                    
                    <aside class="links-block m-5">
                        <h2 class="links-block__caption links-caption">Ближайшее мероприятие</h2>
                        <ul class="links-block__list">
                            <script async src="https://telegram.org/js/telegram-widget.js?15" data-telegram-post="activebike/9" data-width="100%"></script>
                            <!-- <li class="links-block__li tal">
                                <img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/smid_200621_anons.jpg" alt="Наши заезды" class="li-gallery__img">
                                <a href="https://www.dvride.ru/forum/viewtopic.php?pid=401002#p401002" class="links-block__link links-block__link_anons">До Смидовича<br> (20.06.2021 6-00 перед мостом)</a>
                            </li>
                            <li class="links-block__li tal">
                                <img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol200621_anons.jpg" alt="Наши заезды" class="li-gallery__img">
                                <a href="https://www.dvride.ru/forum/viewtopic.php?id=20609" class="links-block__link links-block__link_anons">Волочаевская сопка<br> (20.06.2021 8-30 Платинум Арена)</a>
                            </li> -->
                        </ul>
                    </aside>

                    <!-- <aside class="links-block m-5">
                        <h2 class="links-block__caption links-caption">Последние заезды</h2>
                        <ul class="links-block__list">
                            <li class="links-block__li">
                                <div class="li-gallery owl-carousel">
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/20210619_kv_pens.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                </div>
                                <a href="https://www.dvride.ru/forum/viewtopic.php?pid=400998#p400998" class="links-block__link">
                                    <h3 class="links-block__li-text">"Пенсионерский": Хабаровск - Князе-Волконское - Благодатное - Хабаровск (19.06.2021)</h3>
                                </a>
                            </li>
                            <li class="links-block__li">
                                <div class="li-gallery owl-carousel">
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-1.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-2.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-3.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-4.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-5.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-6.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-7.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-8.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                    <div class="li-gallery__item"><img src="<?php echo get_template_directory_uri() ?>/assets/img/rides_gallery/Vol290521-9.jpg" alt="Наши заезды" class="li-gallery__img"></div>
                                </div>
                                <a href="https://www.strava.com/activities/5375192686" class="links-block__link">
                                    <h3 class="links-block__li-text">Волочаевка (29.05.2021)</h3>
                                </a>
                            </li>
                        </ul>
                    </aside> -->

                    <aside class="links-block">
                        <h2 class="links-block__caption links-caption">Полезные ссылки</h2>
                        <ul class="links-block__list">
                            <li class="links-block__li">
                                <span class="links-block__text">Сообщество ACTIVE BIKE:</span>
                                <span class="social-links">
                                    <a href="https://vk.com/bikekhv" class="social-link social-link_vk" title="Вконтакте"><i class="fa fa-vk fa-lg"></i></a>
                                    <a href="https://www.instagram.com/activebike_khv" class="social-link social-link_instagram" title="Instagram"><i class="fa fa-instagram fa-lg"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <span class="links-block__text">Dvride.Ru (наш форум):</span>
                                <span class="social-links">
                                    <a href="https://www.dvride.ru" class="social-link social-link_dvride" title="Форум Dvride.Ru"><i class="fa fa-bicycle fa-lg"></i></a>
                                    <a href="https://t.me/dvride" class="social-link social-link_telegram" title="чат ВелоХа в Telegram"><i class="fa fa-telegram fa-lg"></i></a>
                                    <a href="https://www.strava.com/clubs/dvride" class="social-link social-link_strava" title="Клуб Dvride в Strava"><i class="icon-strava"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <span class="links-block__text">Чат "Куда поехать":</span>
                                <span class="social-links">
                                    <a href="https://chat.whatsapp.com/Evl24E6CGerETihtyJQtDE" class="social-link social-link_whatsapp" title="WhatsApp"><i class="fa fa-whatsapp fa-lg"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <span class="links-block__text">Туристический клуб "Горизонт":</span>
                                <span class="social-links">
                                    <a href="https://vk.com/togu_gorizont" class="social-link social-link_vk" title="Вконтакте"><i class="fa fa-vk fa-lg"></i></a>
                                    <a href="https://instagram.com/tc_gorizont_khv" class="social-link social-link_instagram" title="Instagram"><i class="fa fa-instagram fa-lg"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <span class="links-block__text">Веломастерская "Вел.Ком" @nefelim1988:</span>
                                <span class="social-links">
                                    <a href="https://www.instagram.com/velcomebike" class="social-link social-link_instagram" title="Instagram"><i class="fa fa-instagram fa-lg"></i></a>
                                    <a href="https://www.strava.com/clubs/velcombike" class="social-link social-link_strava" title="Strava"><i class="icon-strava"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <span class="links-block__text">Веломастерская @velomaster27 (Nick_NeoCOM):</span>
                                <span class="social-links">
                                    <a href="https://www.instagram.com/velomaster27/" class="social-link social-link_instagram" title="Instagram"><i class="fa fa-instagram fa-lg"></i></a>
                                </span>
                            </li>
                            <li class="links-block__li">
                                <a href="https://rudolf-khb.livejournal.com/124304.html" class="link">Веломаршруты по окрестностям Хабаровска (Rudolf)</a>
                            </li>
                        </ul>
                    </aside>
                    <!-- <aside class="links-block">
                    <h2 class="links-block__caption links-caption">Последние заезды в Strava:</h2>
                    <?php echo do_shortcode( "[activities]", true ) ?>
                    </aside> -->

            </div>

                <div class="col-12 col-md-8">
                    <div class="content">
                        <article class="activities">

                            <h2 class="activities__h2"><span class="activities__h2_1">План мероприятий</span> <span class="activities__h2_2">на 2022 год</span></h2>

                            <div class="activities__content">
                                <div class="activity">
                                    <h3 class="activity__caption">Весенний бревет 200 км</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">апрель 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="https://www.dvride.ru/forum/viewtopic.php?id=20505" class="activities__link-link">Обсуждение</a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                            Традиция весенних бреветов вокруг Хабаровска положена <a href="//rudolf-khb.livejournal.com/2095.html" class="link">в 2011 году Павлом Бакановым</a>.  
                                            Бревет - организованный зачётный (с лимитом времени) велозаезд на длинную дистанцию. Стандартными дистанциями являются 200, 300, 400, 600, 1000 и 1200 км. 
                                            Рандоннёр — велосипедист, принимающий участие в специальных заездах, известных как бреветы. 
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Предоткрытие велосезона</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">апрель 2022</div>
                                    <div class="activity__links">
                                    <!-- <a href="https://www.dvride.ru/forum/viewtopic.php?id=20542" class="activities__link-link">Обсуждение</a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Предоткрытие сезона - традиционная массовая покатушка на Пемзенскую протоку, около поселка Владимировка, где в середине апреля можно наблюдать ледоход на Амуре. 
                                            Расстояние небольшое - около 60 км от центра города. 
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Открытие велосезона</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">апрель 2022</div>
                                    <div class="activity__links">
                                    <!-- <a href="https://www.dvride.ru/forum/viewtopic.php?id=20526" class="activities__link-link">Отчет</a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Традиционное открытие летнего велосезона. Мероприятие проводится с целью приобщения людей к велоспорту и активному образу жизни в целом. Примерная дистанция (в одну сторону): до "Ерофей Арены" - 10 км, до Сопки Двух Братьев - 26 км.
                                           Движение по дорогам - согласно ПДД, группами не более 20 человек, наличие включенных передних и задних фонарей при этом - обязательно.
                                           Наличие шлема и защитной экипировки приветствуется.
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>
                               
                                <div class="activity">
                                    <h3 class="activity__caption">Весенняя новичковая 120-ка</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">май 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="https://www.dvride.ru/forum/viewtopic.php?id=20557" class="activities__link-link">Обсуждение: Dvride.Ru</a>
                                        <a href="https://orgeo.ru/event/16845" class="activities__link-link">Регистрация: Orgeo.ru</a> -->
                                        <a href="https://rudolf-khb.livejournal.com/126432.html" class="activities__link-link">Отчет в ЖЖ</a>
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Цель мероприятия - привлечение новых участников к заездам на длинные дистанции. Дистанция 120 км заезда составляет 120 км, и должна быть преодолена за 8 часов, что соответствует формату бреветов (из расчета 15 км в час). В первую очередь приглашаются те, для кого преодоление расстояния выше 100 км будет вызовом самому себе.
                                            На старте будут выданы подробные карты и номерки. Это не соревнование и не гонка, призов за первые места не будет, но ради интереса время прохождения дистанции будет фиксироваться.
                                            На маршруте будут действовать контрольные пункты, где нужно будет получить отметку, а также можно пополнить запасы воды и бананов.
                                            Всем, кто уложится в норматив 8 часов - будут вручены памятные медали.
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">ГранФондо Июнь</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">июнь 2022</div>
                                    <div class="activity__links">
                                    <!-- <a href="https://www.dvride.ru/forum/viewtopic.php?id=20589" class="activities__link-link">Обсуждение: Dvride.Ru</a>    
                                    <a href="https://orgeo.ru/event/17274" class="activities__link-link">Регистрация: Orgeo.ru</a> -->
                                    <a href="https://rudolf-khb.livejournal.com/126661.html" class="activities__link-link">Отчет в ЖЖ</a>
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Массовое мероприятие в формате преодоления стокилометровой дистанции, половина которой проходит по грунтовым дорогам. 
                                            Основная цель - поиск новых оригинальных маршрутов, тренировка новичков, развитие навыков ориентирования.
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>




                                <div class="activity">
                                    <h3 class="activity__caption">ГранФондо Июль</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">июль 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link">
                                        <a href="https://orgeo.ru/event/17636" class="activities__link-link">Регистрация: Orgeo.ru</a>     -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Массовое мероприятие в формате преодоления стокилометровой дистанции, половина которой проходит по грунтовым дорогам. 
                                            Основная цель - поиск новых оригинальных маршрутов, тренировка новичков, развитие навыков ориентирования. 
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Поездка на "озеро Лотосов"</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">июль 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Неспешная покатушка, рассчитанная на новичков. Проходит во время цветения лотосов на озере около поселка Галкино.
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Гонка "Парк северный"</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">август 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Любительская велогонка в Северном парке. 
                                            К гонке допускаются участники от 18 лет при обязательном наличии шлема и исправного велосипеда.
                                            Гонка проходит в формате "1 час" - старт будет открыт в течение 1 часа. В течение этого времени, участники, по завершении очередного круга, могут ехать на следующий круг. Побеждает проехавший большее количество кругов (при равенстве кругов, выше в рейтинге проехавший быстрее).
                                            
                                            <a href="https://www.dvride.ru/forum/viewtopic.php?id=19616" class="link">Обсуждение и результаты гонки 2019 года</a>
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">ГранФондо Август</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">август 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Массовое мероприятие в формате преодоления стокилометровой дистанции, половина которой проходит по грунтовым дорогам. 
                                            Основная цель - поиск новых оригинальных маршрутов, тренировка новичков, развитие навыков ориентирования. 
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Велоквест "Факториал"</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">август 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                        Спортивно-интеллектуальная гонка, которой участвуют команды, в составе которых от 1 до 2 человек. Участники могут передвигаться только на велосипеде. Задача команды - набрать максимальное число баллов за минимальное время. Баллы даются за посещение контрольных пунктов (КП) и за решение задач в контрольных пунктах.
                                            Обсуждение прошлогоднего события: <a href="https://www.dvride.ru/forum/viewtopic.php?id=20360" class="link">Велоквест Факториал 2020</a>
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Гонка ХСО</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">сентябрь 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                            "Кросс-кантри" - гонка по короткому треку с техничными участками. Проводится недалеко от Ильинки, около базы подготовки лыжников.
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                <div class="activity">
                                    <h3 class="activity__caption">Закрытие велосезона</h3>
                                    <div class="activity__icons"><span class="icon-bike"></span></div>
                                    <div class="activity__date">октябрь 2022</div>
                                    <div class="activity__links">
                                        <!-- <a href="" class="activities__link-link"></a> -->
                                    </div>
                                    <div class="activity-descr">
                                        <p class="activity-descr__text">
                                            Традиционная массовая покатушка на Воронежские сопки. Посиделки у костра в осеннем лесу. 
                                        </p>
                                    </div>
                                    <!------------------------- КОНЕЦ ОПИСАНИЯ МЕРОПРИЯТИЯ ----------------------------------->
                                </div>

                                

                            </div>

                        </article>

                    </div>
                </div>

               
        </div>
            <!-- <div class="row">
                <div class="col-12">
                    <div class="weather-info">
                        <iframe width="100%" height="200" src="https://embed.windy.com/embed2.html?lat=48.396&lon=135.044&detailLat=48.480&detailLon=135.080&width=650&height=450&zoom=8&level=surface&overlay=wind&product=ecmwf&menu=&message=true&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=m%2Fs&metricTemp=%C2%B0C&radarRange=-1"
                            frameborder="0"></iframe>
                    </div>
                </div>
            </div> -->
    </div>

    <div style="display: none;">
    <?php
    if ( have_posts() ) :

        if ( is_home() && ! is_front_page() ) :
            ?>
            <!-- <header>
                <h1 class="page-title screen-reader-text"><?php single_post_title(); ?></h1>
            </header> -->
            <?php
        endif;

        /* Start the Loop */
        while ( have_posts() ) :
            the_post();

            /*
                * Include the Post-Type-specific template for the content.
                * If you want to override this in a child theme, then include a file
                * called content-___.php (where ___ is the Post Type name) and that will be used instead.
                */
            get_template_part( 'template-parts/content', get_post_type() );

        endwhile;

        the_posts_navigation();

    else :

        get_template_part( 'template-parts/content', 'none' );

    endif;
    ?>

    </div>

	</main><!-- #main -->

<?php
//get_sidebar();
get_footer();
