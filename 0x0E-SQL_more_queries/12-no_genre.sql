-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT show.`title`, gen.`genre_id`
  FROM `tv_shows` AS show
    LEFT JOIN `tv_show_genres` AS gen
    ON show.`title` = gen.`genre_id`
    WHERE gen.`genre_id` IS NULL
ORDER BY show.`title`, gen.`genre_id`;
