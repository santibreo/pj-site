library(data.table)
library(scales)
library(ggplot2)
library(ggpubr)
library(dplyr)

# Define begining date ----
init_date <- as.Date("2020-01-20")

# Get daily data ----
link <- "blob:https://ourworldindata.org/1eee483c-e51c-424d-9f4f-3ab634eaf0d9"
daily_cases <- fread("data/daily-cases-covid-19-who.csv")
# Rename columns ----
colnames(daily_cases) <- make.names(colnames(daily_cases))
daily_cases <- daily_cases[
    ,.(country=Entity, ord=Year, cases=Daily.new.confirmed.cases.of.COVID.19),
    ]
daily_cases$day <- init_date + daily_cases$ord

# Get total data ----
link <- "blob:https://ourworldindata.org/ca5d8db3-2011-4689-8af6-a18d2ea8901f"
total_cases <- fread("data/total-cases-covid-19-who.csv")
# Rename columns ----
colnames(total_cases) <- make.names(colnames(total_cases))

total_cases <- total_cases[
    ,.(country=Entity, ord=Year, cases=Total.confirmed.cases.of.COVID.19),
    ]
total_cases$day <- init_date + total_cases$ord

# GLobal plot ----
selected_countries <- c(
    "China",
    "Iran",
    "Italy",
    "South Korea",
    "Spain",
    "Worldwide" 
    )

p1 <- total_cases %>%
    filter(country %in% selected_countries) %>%
    ggplot(aes(x = day, y = cases, fill=country)) +
    geom_vline(xintercept = as.Date("2020-02-21"), linetype=4, colour="black") +
    geom_line(aes(color=country), show.legend=FALSE) +
    geom_point(aes(color=country), show.legend=FALSE) +
    labs(title="Total number of cases", y="total cases", x="date") +
    scale_y_continuous(labels = scales::unit_format(unit = "k", scale = 1e-3)) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )

p2 <- daily_cases %>%
    filter(country %in% selected_countries) %>%
    ggplot(aes(x = day, y = cases, fill=country)) +
    geom_vline(xintercept = as.Date("2020-02-21"), linetype=4, colour="black") +
    geom_line(aes(color=country)) +
    geom_point(aes(color=country)) +
    labs(title="Daily number of cases", y="daily cases", x="date") +
    scale_y_continuous(labels = scales::unit_format(unit = "K", scale = 1e-3)) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )

png("static/2020/covid-19-disease/complete.png", width=1000, height=650,
    res = 120, bg=NA, units="px")
ggarrange(
    p1, p2, common.legend = TRUE, legend = "bottom"
)
dev.off()

# Correct the data ----
daily_cases_exp <- setnafill(
    dcast(daily_cases, day + ord ~ country, value.var = "cases"), fill=0
)
# With dates
c_daily_cases <- daily_cases_exp[day >= as.Date("2020-02-21"),]

# Remove China
c_daily_cases[["World-China"]] <- c_daily_cases$Worldwide - c_daily_cases$China

# Rebuild original data ----
daily_cases <- melt(
    c_daily_cases,
    measure.vars = colnames(c_daily_cases)[3:ncol(c_daily_cases)],
    variable.name = "country",
    value.name = "cases"
)

# Correct the data ----
total_cases_exp <- setnafill(
    dcast(total_cases, day + ord ~ country, value.var = "cases"), fill=0
)
c_total_cases <- total_cases_exp[day >= as.Date("2020-02-21"),]
c_total_cases[["World-China"]] <- c_total_cases$Worldwide - c_total_cases$China

# Rebuild original data ----
total_cases <- melt(
    c_total_cases,
    measure.vars = colnames(c_total_cases)[3:ncol(c_total_cases)],
    variable.name = "country",
    value.name = "cases"
)

# But China plot ----
selected_countries <- c(
    "Iran",
    "Italy",
    "South Korea",
    "Spain",
    "World-China" 
)

p1 <- total_cases %>%
    filter(country %in% selected_countries) %>%
    ggplot(aes(x = day, y = cases, fill=country)) +
    geom_line(aes(color=country), show.legend=FALSE) +
    geom_point(aes(color=country), show.legend=FALSE) +
    labs(title="Total number of cases", y="total cases", x="date") +
    scale_y_continuous(labels = scales::unit_format(unit = "k", scale = 1e-3)) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )

p2 <- daily_cases %>%
    filter(country %in% selected_countries) %>%
    ggplot(aes(x = day, y = cases, fill=country)) +
    geom_line(aes(color=country)) +
    geom_point(aes(color=country)) +
    labs(title="Daily number of cases", y="daily cases", x="date") +
    scale_y_continuous(labels = scales::unit_format(unit = "K", scale = 1e-3)) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )

png("static/2020/covid-19-disease/butchina.png", width=1000, height=650,
    res = 120, bg=NA, units="px")
ggarrange(
    p1, p2, common.legend = TRUE, legend = "bottom"
)
dev.off()

# Linear regression ----
total_regr_data <- c_total_cases[, c("day", "ord")]
total_regr_data$`World-China_log` <- log(c_total_cases$`World-China`)
linearMod <- lm(`World-China_log` ~ ord, data=total_regr_data)
summary(linearMod)
p1 <- total_regr_data %>%
    ggplot(aes(x = day, y = `World-China_log`)) +
    geom_point(show.legend=FALSE) +
    labs(title="Total number of cases", y="total cases", x="date") +
    geom_abline(intercept = -3337.5003892, slope = 0.1826481,linetype=1, colour="red") +
    scale_y_continuous(labels = trans_format("exp", math_format(.x))) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )


daily_regr_data <- c_daily_cases[, c("day", "ord")]
daily_regr_data$`World-China_log` <- log(c_daily_cases$`World-China`)
linearMod <- lm(`World-China_log` ~ ord, data=daily_regr_data)
summary(linearMod)
p2 <- daily_regr_data %>%
    ggplot(aes(x = day, y = `World-China_log`)) +
    geom_point(show.legend=FALSE) +
    labs(title="Daily number of cases", y="daily cases", x="date") +
    geom_abline(intercept = -3105.307230, slope = 0.169876,linetype=1, colour="red") +
    scale_y_continuous(labels = trans_format("exp", math_format(.x))) +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )

png("static/2020/covid-19-disease/linearregs.png", width=1000, height=650,
    res = 120, bg=NA, units="px")
ggarrange(
    p1, p2, common.legend = TRUE, legend = "bottom"
)
dev.off()

# Set R0 data ----
R0_data <- c_total_cases[, c("day", "ord")]
for(col in selected_countries){
    set(R0_data, , col, c_total_cases[[col]] / shift(c_total_cases[[col]]) - 1)
}
R0_data <- setnafill(R0_data, fill = 0)
R0_data <- melt(
    R0_data,
    measure.vars = colnames(R0_data)[3:ncol(R0_data)],
    variable.name = "country",
    value.name = "cases"
)

png("static/2020/covid-19-disease/r0evol.png", width=1000, height=650,
    res = 120, bg=NA, units="px")
R0_data %>%
    filter(country %in% selected_countries) %>%
    ggplot(aes(x = day, y = cases, fill=country)) +
    geom_line(aes(color=country)) +
    geom_point(aes(color=country)) +
    labs(title="R0 evolution", y="daily cases", x="date") +
    scale_x_date(date_breaks = "1 week",
                 date_minor_breaks = "1 day",
                 date_labels = "%b %d") +
    theme(
        panel.background = element_rect(fill = "transparent"), # bg of the panel
        plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
        legend.background = element_rect(fill = "transparent"), # get rid of legend bg
        legend.box.background = element_rect(fill = "transparent") # get rid of legend panel bg
    )
dev.off()

# Growth factor ----
c_daily_cases$`World-China` / shift(c_daily_cases$`World-China`)
 