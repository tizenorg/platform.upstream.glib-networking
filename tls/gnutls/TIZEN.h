#ifndef TIZEN_H
#define TIZEN_H

#define ENABLE(TIZEN_FEATURE) (defined ENABLE_##TIZEN_FEATURE  && ENABLE_##TIZEN_FEATURE)

#define ENABLE_TIZEN_TLS11_AND_TLS12_SUPPORT_DISABLE 1

#define ENABLE_TIZEN_NPN 1

#if ENABLE(TIZEN_TV_DLOG)

#ifndef LOG_TAG
#define LOG_TAG "glib-networking" /* This LOG_TAG should be defined before including dlog.h. Because dlog.h is using it. */
#endif

#include <dlog/dlog.h>

#define TIZEN_LOGD(fmt, args...) LOGD("[%s: %s: %d] "fmt, (rindex(__FILE__, '/') ? rindex(__FILE__, '/') + 1 : __FILE__), __FUNCTION__, __LINE__, ##args)
#define TIZEN_LOGI(fmt, args...) LOGI("[%s: %s: %d] "fmt, (rindex(__FILE__, '/') ? rindex(__FILE__, '/') + 1 : __FILE__), __FUNCTION__, __LINE__, ##args)
#define TIZEN_LOGW(fmt, args...) LOGW("[%s: %s: %d] "fmt, (rindex(__FILE__, '/') ? rindex(__FILE__, '/') + 1 : __FILE__), __FUNCTION__, __LINE__, ##args)
#define TIZEN_LOGE(fmt, args...) LOGE("[%s: %s: %d] "fmt, (rindex(__FILE__, '/') ? rindex(__FILE__, '/') + 1 : __FILE__), __FUNCTION__, __LINE__, ##args)
#define TIZEN_LOGE_IF(cond, fmt, args...) LOGE_IF(cond, "[%s: %s: %d] "fmt, (rindex(__FILE__, '/') ? rindex(__FILE__, '/') + 1 : __FILE__), __FUNCTION__, __LINE__, ##args)

#endif

#endif
