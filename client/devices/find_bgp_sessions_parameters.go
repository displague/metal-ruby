// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"
)

// NewFindBgpSessionsParams creates a new FindBgpSessionsParams object
// with the default values initialized.
func NewFindBgpSessionsParams() *FindBgpSessionsParams {
	var ()
	return &FindBgpSessionsParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindBgpSessionsParamsWithTimeout creates a new FindBgpSessionsParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindBgpSessionsParamsWithTimeout(timeout time.Duration) *FindBgpSessionsParams {
	var ()
	return &FindBgpSessionsParams{

		timeout: timeout,
	}
}

// NewFindBgpSessionsParamsWithContext creates a new FindBgpSessionsParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindBgpSessionsParamsWithContext(ctx context.Context) *FindBgpSessionsParams {
	var ()
	return &FindBgpSessionsParams{

		Context: ctx,
	}
}

// NewFindBgpSessionsParamsWithHTTPClient creates a new FindBgpSessionsParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindBgpSessionsParamsWithHTTPClient(client *http.Client) *FindBgpSessionsParams {
	var ()
	return &FindBgpSessionsParams{
		HTTPClient: client,
	}
}

/*FindBgpSessionsParams contains all the parameters to send to the API endpoint
for the find bgp sessions operation typically these are written to a http.Request
*/
type FindBgpSessionsParams struct {

	/*ID
	  Device UUID

	*/
	ID strfmt.UUID

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find bgp sessions params
func (o *FindBgpSessionsParams) WithTimeout(timeout time.Duration) *FindBgpSessionsParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find bgp sessions params
func (o *FindBgpSessionsParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find bgp sessions params
func (o *FindBgpSessionsParams) WithContext(ctx context.Context) *FindBgpSessionsParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find bgp sessions params
func (o *FindBgpSessionsParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find bgp sessions params
func (o *FindBgpSessionsParams) WithHTTPClient(client *http.Client) *FindBgpSessionsParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find bgp sessions params
func (o *FindBgpSessionsParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the find bgp sessions params
func (o *FindBgpSessionsParams) WithID(id strfmt.UUID) *FindBgpSessionsParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find bgp sessions params
func (o *FindBgpSessionsParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *FindBgpSessionsParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}